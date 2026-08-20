"""Kommandozeile.

    python -m ytfc.cli poll      neue Videos aus den RSS-Feeds holen
    python -m ytfc.cli check     offene Videos transkribieren und pruefen
    python -m ytfc.cli run       poll + check
    python -m ytfc.cli review    Befunde durchsehen und ggf. posten
    python -m ytfc.cli whoami    OAuth-Selbsttest
    python -m ytfc.cli show ID   Bericht eines Videos anzeigen
"""

from __future__ import annotations

import argparse
import sys
import textwrap

from . import config as config_mod
from . import feeds, report, state, transcript
from .factcheck import Checked, Claim, FactChecker, Report

BOLD, DIM, RED, YEL, GRN, OFF = (
    "\033[1m", "\033[2m", "\033[31m", "\033[33m", "\033[32m", "\033[0m"
)


def _log(msg: str, indent: int = 0) -> None:
    print(" " * indent + msg, flush=True)


# --- poll ------------------------------------------------------------------


def cmd_poll(cfg, st: state.State, args) -> int:
    found = 0
    for ch in cfg.channels:
        cid = ch.channel_id or st.cached_channel_id(ch.handle)
        if not cid:
            try:
                cid = feeds.resolve_channel_id(ch.handle)
            except Exception as e:
                _log(f"{RED}✗{OFF} {ch.name}: {e}")
                continue
            st.remember_channel(cid, ch.handle, ch.name)
            _log(f"{DIM}  {ch.handle} -> {cid}{OFF}")

        try:
            entries = feeds.recent(feeds.fetch_feed(cid), cfg.lookback_hours)
        except Exception as e:
            _log(f"{RED}✗{OFF} {ch.name}: Feed nicht erreichbar ({e})")
            continue

        new = [e for e in entries if not st.is_known(e["video_id"])]
        for e in new:
            st.add_video({
                "video_id": e["video_id"], "channel_id": cid,
                "channel_name": ch.name, "risk": ch.risk,
                "title": e["title"], "published": e["published"],
            })
        found += len(new)
        _log(f"{GRN}✓{OFF} {ch.name}: {len(new)} neu "
             f"{DIM}({len(entries)} im Zeitfenster){OFF}")
    _log(f"\n{BOLD}{found} neue Videos{OFF}")
    return 0


# --- check -----------------------------------------------------------------


def _check_one(cfg, st: state.State, row, fc: FactChecker) -> None:
    vid, risk = row["video_id"], row["risk"]
    _log(f"\n{BOLD}▶ {row['title']}{OFF}")
    _log(f"{DIM}{row['channel_name']} · {risk} · youtu.be/{vid}{OFF}")

    channel_cfg = next(
        (c for c in cfg.channels if c.name == row["channel_name"]), None
    )
    languages = channel_cfg.languages if channel_cfg else ["de", "en"]

    try:
        tr = transcript.fetch(vid, languages, cfg.transcript)
    except transcript.TranscriptUnavailable as e:
        _log(f"{YEL}⚠ kein Transkript{OFF}", 2)
        st.set_status(vid, state.STATUS_NO_TRANSCRIPT, str(e))
        return
    _log(f"{DIM}Transkript: {tr.word_count} Woerter via {tr.source}{OFF}", 2)

    text = tr.as_prompt_text()
    topic, claims = fc.extract_claims(text, row["title"], cfg.max_claims(risk))
    _log(f"{DIM}{len(claims)} pruefbare Behauptungen{OFF}", 2)
    if not claims:
        st.set_status(vid, state.STATUS_CLEAN, "keine pruefbaren Behauptungen")
        return

    rep = Report(video_id=vid, title=row["title"], channel=row["channel_name"],
                 risk=risk, topic=topic, transcript_source=tr.source)
    for i, cl in enumerate(claims, 1):
        _log(f"{DIM}[{i}/{len(claims)}] {cl.claim[:70]}…{OFF}", 2)
        try:
            res = fc.check_claim(cl, row["title"], row["channel_name"],
                                 cfg.effort(risk), cfg.min_sources(risk))
        except Exception as e:
            _log(f"{RED}  Fehler: {e}{OFF}", 4)
            continue
        mark = report.MARKER[res.verdict]
        _log(f"{mark} {report.LABEL[res.verdict]} {DIM}({res.confidence}){OFF}", 6)
        rep.checked.append(res)

    if cfg.wants_rhetoric(risk):
        _log(f"{DIM}Einordnung der Darstellung…{OFF}", 2)
        rep.rhetoric = fc.analyse_rhetoric(text, row["title"])

    rep.usage = dict(fc.usage)
    path = report.write_markdown(rep, cfg.reports_dir)
    st.save_report(vid, _report_to_dict(rep), str(path))
    st.set_status(
        vid,
        state.STATUS_CHECKED if rep.problems else state.STATUS_CLEAN,
        f"{len(rep.problems)} auffaellig von {len(rep.checked)}",
    )
    flag = f"{RED}{len(rep.problems)} auffaellig{OFF}" if rep.problems \
        else f"{GRN}nichts zu melden{OFF}"
    _log(f"{flag} → {path.name}", 2)


def cmd_check(cfg, st: state.State, args) -> int:
    rows = st.pending(state.STATUS_NEW, args.limit)
    if not rows:
        _log("Nichts offen.")
        return 0
    fc = FactChecker(cfg.model)
    for row in rows:
        try:
            _check_one(cfg, st, row, fc)
        except KeyboardInterrupt:
            _log("\nAbgebrochen.")
            return 130
        except Exception as e:
            _log(f"{RED}✗ {row['video_id']}: {e}{OFF}")
            st.set_status(row["video_id"], state.STATUS_ERROR, str(e))
    u = fc.usage
    _log(f"\n{DIM}{u['calls']} Claude-Aufrufe · {u['input']:,} in / "
         f"{u['output']:,} out{OFF}")
    return 0


# --- review / post ---------------------------------------------------------


def cmd_review(cfg, st: state.State, args) -> int:
    from . import youtube_post

    ccfg = cfg.comment_cfg
    rows = st.pending(state.STATUS_CHECKED, 50)
    if not rows:
        _log("Keine offenen Befunde.")
        return 0

    only = tuple(ccfg.get("only_post_if", ["falsch", "irrefuehrend"]))
    limit = int(ccfg.get("max_per_day", 3))

    for row in rows:
        rep = _dict_to_report(st.report(row["video_id"]))
        if rep is None:
            continue
        body = report.to_comment(rep, int(ccfg.get("max_chars", 9000)), only)

        print(f"\n{'═' * 72}")
        print(f"{BOLD}{rep.title}{OFF}")
        print(f"{DIM}{rep.channel} · youtu.be/{rep.video_id}{OFF}\n")
        for c in rep.checked:
            print(f"  {report.MARKER[c.verdict]} {c.claim.timestamp} "
                  f"{report.LABEL[c.verdict]} {DIM}({c.confidence}){OFF}")
            print(textwrap.indent(textwrap.fill(c.one_liner, 66), "     "))
        if not body:
            print(f"\n{DIM}Kein Befund, der einen Kommentar rechtfertigt.{OFF}")
            st.set_status(rep.video_id, state.STATUS_CLEAN)
            continue

        print(f"\n{BOLD}Kommentarentwurf ({len(body)} Zeichen):{OFF}")
        print(f"{DIM}{'─' * 72}{OFF}")
        print(body)
        print(f"{DIM}{'─' * 72}{OFF}")

        if not ccfg.get("enabled"):
            print(f"{YEL}Posten ist in der Config deaktiviert "
                  f"(publish.youtube_comment.enabled).{OFF}")
            continue
        if st.posts_today() >= limit:
            print(f"{YEL}Tageslimit von {limit} Kommentaren erreicht.{OFF}")
            break

        choice = input(f"\n{BOLD}Posten? [j]a / [n]ein / [ü]berspringen: "
                       f"{OFF}").strip().lower()
        if choice in ("n", "nein"):
            st.set_status(rep.video_id, state.STATUS_CLEAN, "verworfen")
            continue
        if choice not in ("j", "ja", "y"):
            continue
        try:
            cid = youtube_post.post_comment(cfg.root, rep.video_id, body,
                                            approved=True)
        except Exception as e:
            _log(f"{RED}✗ Posten fehlgeschlagen: {e}{OFF}")
            continue
        st.record_post(rep.video_id, cid, body)
        st.set_status(rep.video_id, state.STATUS_POSTED)
        _log(f"{GRN}✓ gepostet{OFF} {DIM}({cid}){OFF}")
    return 0


def cmd_whoami(cfg, st, args) -> int:
    from . import youtube_post

    me = youtube_post.my_channel(cfg.root)
    _log(f"Angemeldet als: {BOLD}{me['title']}{OFF} {DIM}({me['id']}){OFF}")
    _log(f"{DIM}Kommentare heute: {st.posts_today()}{OFF}")
    return 0


def cmd_show(cfg, st: state.State, args) -> int:
    payload = st.report(args.video_id)
    if not payload:
        _log(f"Kein Bericht fuer {args.video_id}.")
        return 1
    print(report.to_markdown(_dict_to_report(payload)))
    return 0


# --- (De-)Serialisierung ---------------------------------------------------


def _report_to_dict(r: Report) -> dict:
    return {
        "video_id": r.video_id, "title": r.title, "channel": r.channel,
        "risk": r.risk, "topic": r.topic,
        "transcript_source": r.transcript_source,
        "rhetoric": r.rhetoric, "usage": r.usage,
        "checked": [
            {
                "claim": vars(c.claim), "verdict": c.verdict,
                "confidence": c.confidence, "one_liner": c.one_liner,
                "explanation": c.explanation, "what_is_true": c.what_is_true,
                "sources": c.sources, "research_notes": c.research_notes,
            }
            for c in r.checked
        ],
    }


def _dict_to_report(d: dict | None) -> Report | None:
    if not d:
        return None
    r = Report(
        video_id=d["video_id"], title=d["title"], channel=d["channel"],
        risk=d["risk"], topic=d["topic"],
        transcript_source=d["transcript_source"],
        rhetoric=d.get("rhetoric", ""), usage=d.get("usage", {}),
    )
    r.checked = [
        Checked(claim=Claim(**c["claim"]), verdict=c["verdict"],
                confidence=c["confidence"], one_liner=c["one_liner"],
                explanation=c["explanation"], what_is_true=c["what_is_true"],
                sources=c["sources"], research_notes=c.get("research_notes", ""))
        for c in d["checked"]
    ]
    return r


# --- main ------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="ytfc", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--config", help="Pfad zur config.yaml")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("poll", help="neue Videos finden")
    c = sub.add_parser("check", help="offene Videos pruefen")
    c.add_argument("--limit", type=int, default=5)
    r = sub.add_parser("run", help="poll + check")
    r.add_argument("--limit", type=int, default=5)
    sub.add_parser("review", help="Befunde durchsehen und posten")
    sub.add_parser("whoami", help="OAuth-Selbsttest")
    s = sub.add_parser("show", help="Bericht anzeigen")
    s.add_argument("video_id")

    args = p.parse_args(argv)
    cfg = config_mod.load(args.config)
    st = state.State(cfg.db_path)

    if args.cmd == "run":
        rc = cmd_poll(cfg, st, args)
        return rc or cmd_check(cfg, st, args)
    return {
        "poll": cmd_poll, "check": cmd_check, "review": cmd_review,
        "whoami": cmd_whoami, "show": cmd_show,
    }[args.cmd](cfg, st, args)


if __name__ == "__main__":
    sys.exit(main())
