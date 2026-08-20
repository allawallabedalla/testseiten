"""Transkript besorgen — drei Stufen, von billig nach teuer.

1. ``youtube-transcript-api``  — die von YouTube ausgelieferten Untertitel.
2. ``yt-dlp``                  — Auto-Untertitel als VTT, wenn (1) blockt.
3. ``faster-whisper``          — Tonspur selbst transkribieren (optional).

Die offizielle YouTube Data API kann Untertitel nur fuer *eigene* Videos
herunterladen, deshalb kommt sie hier nicht vor.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

_TIMESTAMP_RE = re.compile(
    r"(\d{2}):(\d{2}):(\d{2})[.,](\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2})"
)
_TAG_RE = re.compile(r"<[^>]+>")


class TranscriptUnavailable(RuntimeError):
    """Kein Transkript beschaffbar — kein Fehler, sondern ein Zustand."""


@dataclass
class Segment:
    start: float
    text: str

    @property
    def stamp(self) -> str:
        m, s = divmod(int(self.start), 60)
        h, m = divmod(m, 60)
        return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:d}:{s:02d}"


@dataclass
class Transcript:
    segments: list[Segment]
    source: str
    language: str | None = None

    def as_prompt_text(self) -> str:
        """Zeitgestempelt, damit Claude jede Behauptung verorten kann."""
        return "\n".join(f"[{s.stamp}] {s.text}" for s in self.segments)

    @property
    def word_count(self) -> int:
        return sum(len(s.text.split()) for s in self.segments)

    def seconds_for_stamp(self, stamp: str) -> int:
        parts = [int(p) for p in stamp.split(":")]
        while len(parts) < 3:
            parts.insert(0, 0)
        return parts[0] * 3600 + parts[1] * 60 + parts[2]


# --- Stufe 1: youtube-transcript-api ---------------------------------------


def _via_transcript_api(video_id: str, languages: list[str]) -> Transcript | None:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        return None

    raw = None
    # v1.x: Instanz + .fetch(); v0.x: Klassenmethode .get_transcript()
    try:
        raw = YouTubeTranscriptApi().fetch(video_id, languages=languages)
    except AttributeError:
        pass
    except Exception:
        return None
    if raw is None:
        try:
            raw = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        except Exception:
            return None

    segments, lang = [], getattr(raw, "language_code", None)
    for item in raw:
        if isinstance(item, dict):
            start, text = item.get("start", 0.0), item.get("text", "")
        else:
            start, text = getattr(item, "start", 0.0), getattr(item, "text", "")
        text = text.replace("\n", " ").strip()
        if text:
            segments.append(Segment(float(start), text))
    return Transcript(segments, "youtube-transcript-api", lang) if segments else None


# --- Stufe 2: yt-dlp Auto-Untertitel ---------------------------------------


def _parse_vtt(path: Path) -> list[Segment]:
    segments: list[Segment] = []
    start: float | None = None
    # Auto-Untertitel "rollen": jede Cue wiederholt die Vorzeile mit einem
    # NEUEN Zeitstempel. Deshalb nur gegen die zuletzt ausgegebenen Zeilen
    # vergleichen, nicht gegen (Zeit, Text) — sonst steht alles doppelt drin.
    recent: list[str] = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = _TIMESTAMP_RE.search(line)
        if m:
            h, mi, s, ms = (int(m.group(i)) for i in (1, 2, 3, 4))
            start = h * 3600 + mi * 60 + s + ms / 1000
            continue
        line = _TAG_RE.sub("", line).strip()
        if not line or start is None or line.startswith(("WEBVTT", "Kind:", "Language:")):
            continue
        if line in recent:
            continue
        recent.append(line)
        del recent[:-4]
        segments.append(Segment(start, line))
    return segments


def _via_ytdlp(video_id: str, languages: list[str]) -> Transcript | None:
    if not shutil.which("yt-dlp"):
        return None
    langs = ",".join(languages)
    with tempfile.TemporaryDirectory() as tmp:
        cmd = [
            "yt-dlp", "--skip-download",
            "--write-subs", "--write-auto-subs",
            "--sub-langs", f"{langs},{langs.split(',')[0]}-orig",
            "--sub-format", "vtt", "--convert-subs", "vtt",
            "-o", f"{tmp}/%(id)s.%(ext)s",
            f"https://www.youtube.com/watch?v={video_id}",
        ]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        files = sorted(Path(tmp).glob("*.vtt"))
        if r.returncode != 0 and not files:
            return None
        for f in files:
            segments = _parse_vtt(f)
            if segments:
                lang = f.stem.split(".")[-1] if "." in f.stem else None
                return Transcript(segments, "yt-dlp", lang)
    return None


# --- Stufe 3: Whisper ------------------------------------------------------


def _via_whisper(video_id: str, model_size: str) -> Transcript | None:
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        return None
    if not shutil.which("yt-dlp"):
        return None

    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / f"{video_id}.m4a"
        r = subprocess.run(
            ["yt-dlp", "-x", "--audio-format", "m4a", "-o", str(out),
             f"https://www.youtube.com/watch?v={video_id}"],
            capture_output=True, text=True, timeout=1800,
        )
        audio = next(iter(Path(tmp).glob(f"{video_id}.*")), None)
        if r.returncode != 0 or audio is None:
            return None
        model = WhisperModel(model_size, compute_type="int8")
        chunks, info = model.transcribe(str(audio), vad_filter=True)
        segments = [
            Segment(float(c.start), c.text.strip()) for c in chunks if c.text.strip()
        ]
    return Transcript(segments, "whisper", info.language) if segments else None


# --- Einstiegspunkt --------------------------------------------------------


def fetch(video_id: str, languages: list[str], cfg: dict) -> Transcript:
    for attempt in (
        lambda: _via_transcript_api(video_id, languages),
        lambda: _via_ytdlp(video_id, languages),
    ):
        try:
            t = attempt()
        except Exception:
            t = None
        if t:
            return t

    if cfg.get("allow_whisper_fallback"):
        try:
            t = _via_whisper(video_id, cfg.get("whisper_model", "small"))
        except Exception:
            t = None
        if t:
            return t

    raise TranscriptUnavailable(
        f"Kein Transkript fuer {video_id}. Wenn das haeufig passiert, laeuft der "
        f"Bot vermutlich auf einer Rechenzentrums-IP, die YouTube blockt — "
        f"oder das Video hat schlicht keine Untertitel (dann Whisper aktivieren)."
    )
