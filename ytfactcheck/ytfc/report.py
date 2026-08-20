"""Berichte: ausfuehrliches Markdown zum Nachlesen, knapper Text zum Posten."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from .factcheck import Report

MARKER = {
    "belegt": "✅",
    "groesstenteils_richtig": "🟢",
    "kontextfehlend": "🟡",
    "irrefuehrend": "⚠️",
    "falsch": "❌",
    "nicht_ueberpruefbar": "❔",
}
LABEL = {
    "belegt": "Belegt",
    "groesstenteils_richtig": "Groesstenteils richtig",
    "kontextfehlend": "Wichtiger Kontext fehlt",
    "irrefuehrend": "Irrefuehrend",
    "falsch": "Falsch",
    "nicht_ueberpruefbar": "Nicht ueberpruefbar",
}


def _ts_link(video_id: str, stamp: str) -> str:
    parts = [int(p) for p in stamp.split(":")] if stamp.replace(":", "").isdigit() else [0]
    while len(parts) < 3:
        parts.insert(0, 0)
    secs = parts[0] * 3600 + parts[1] * 60 + parts[2]
    return f"https://youtu.be/{video_id}?t={secs}"


# --- Markdown --------------------------------------------------------------


def to_markdown(r: Report) -> str:
    lines = [
        f"# Faktencheck: {r.title}",
        "",
        f"- **Kanal:** {r.channel} (Risikostufe: {r.risk})",
        f"- **Video:** https://www.youtube.com/watch?v={r.video_id}",
        f"- **Thema:** {r.topic}",
        f"- **Transkriptquelle:** {r.transcript_source}",
        f"- **Geprueft am:** {datetime.now():%d.%m.%Y %H:%M}",
        f"- **Gepruefte Aussagen:** {len(r.checked)} "
        f"(davon auffaellig: {len(r.problems)})",
        "",
        "> Automatisch erstellt. Jedes Urteil stuetzt sich ausschliesslich auf",
        "> die unten verlinkten Quellen. Vor jeder Weiterverwendung nachlesen.",
        "",
        "## Ergebnisse",
        "",
    ]
    for i, c in enumerate(r.checked, 1):
        lines += [
            f"### {i}. {MARKER[c.verdict]} {LABEL[c.verdict]} "
            f"— [{c.claim.timestamp}]({_ts_link(r.video_id, c.claim.timestamp)})",
            "",
            f"**Behauptung:** {c.claim.claim}",
            "",
            f"> {c.claim.quote}",
            "",
            f"**Kurz:** {c.one_liner}",
            "",
            f"**Bewertung:** {LABEL[c.verdict]} · Quellenlage: {c.confidence}",
            "",
            c.explanation,
            "",
        ]
        if c.what_is_true:
            lines += [f"**Richtig ist:** {c.what_is_true}", ""]
        if c.sources:
            lines.append("**Quellen:**")
            lines += [
                f"- [{s['title']}]({s['url']}) — {s['publisher']} ({s['stance']})"
                for s in c.sources
            ]
        else:
            lines.append("**Quellen:** keine belastbaren gefunden.")
        lines += ["", "<details><summary>Rechercheprotokoll</summary>", "",
                  c.research_notes, "", "</details>", ""]

    if r.rhetoric:
        lines += ["## Einordnung der Darstellung", "",
                  "*Keine Faktenpruefung, sondern eine Beschreibung der "
                  "Argumentationsweise.*", "", r.rhetoric, ""]

    if r.usage:
        lines += [
            "---", "",
            f"<sub>{r.usage.get('calls', 0)} Claude-Aufrufe · "
            f"{r.usage.get('input', 0):,} Input- / "
            f"{r.usage.get('output', 0):,} Output-Tokens</sub>",
        ]
    return "\n".join(lines)


def write_markdown(r: Report, directory: Path) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{datetime.now():%Y-%m-%d}-{r.video_id}.md"
    path.write_text(to_markdown(r), encoding="utf-8")
    return path


# --- YouTube-Kommentar -----------------------------------------------------

FOOTER = (
    "— Erstellt mit KI-Unterstuetzung (Websuche + Quellenpruefung), "
    "vor dem Posten von Hand geprueft. Korrekturen willkommen."
)


def to_comment(r: Report, max_chars: int = 9000,
               only: tuple[str, ...] | None = None) -> str:
    """Kurzfassung fuer ein YouTube-Kommentarfeld (Klartext, kein Markdown)."""
    items = [c for c in r.checked if not only or c.verdict in only]
    if not items:
        return ""
    items.sort(key=lambda c: (c.verdict not in ("falsch", "irrefuehrend"),
                              -c.claim.checkworthiness))

    head = f"Faktencheck zu diesem Video ({len(items)} von {len(r.checked)} " \
           f"geprueften Aussagen auffaellig)\n"
    blocks = []
    for c in items:
        b = [
            f"\n{MARKER[c.verdict]} {c.claim.timestamp} — {LABEL[c.verdict]}",
            f"„{c.claim.quote.strip()}“",
            c.one_liner,
        ]
        if c.what_is_true:
            b.append(f"Richtig: {c.what_is_true}")
        for s in c.sources[:2]:
            b.append(f"Quelle: {s['url']}")
        blocks.append("\n".join(b))

    # Ganze Bloecke fallen lassen statt mitten im Satz abzuschneiden.
    out = head
    for b in blocks:
        if len(out) + len(b) + len(FOOTER) + 8 > max_chars:
            out += f"\n\n(+{len(blocks) - blocks.index(b)} weitere Punkte)"
            break
        out += b + "\n"
    return f"{out}\n{FOOTER}"
