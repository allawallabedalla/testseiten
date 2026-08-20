"""Konfiguration laden und validieren."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml

RISK_LEVELS = ("normal", "erhoeht", "problematisch")


@dataclass
class Channel:
    name: str
    risk: str = "normal"
    handle: str | None = None
    channel_id: str | None = None
    languages: list[str] = field(default_factory=lambda: ["de", "en"])

    def __post_init__(self) -> None:
        if self.risk not in RISK_LEVELS:
            raise ValueError(
                f"Kanal {self.name!r}: risk={self.risk!r} unbekannt, "
                f"erlaubt sind {RISK_LEVELS}"
            )
        if not (self.handle or self.channel_id):
            raise ValueError(f"Kanal {self.name!r}: handle oder channel_id noetig")


@dataclass
class Config:
    model: str
    lookback_hours: int
    channels: list[Channel]
    transcript: dict
    factcheck: dict
    publish: dict
    root: Path

    # --- Ableitungen pro Risikostufe -------------------------------------

    def max_claims(self, risk: str) -> int:
        return int(self.factcheck["max_claims"][risk])

    def effort(self, risk: str) -> str:
        return str(self.factcheck["effort"][risk])

    def min_sources(self, risk: str) -> int:
        return int(self.factcheck["min_sources"][risk])

    def wants_rhetoric(self, risk: str) -> bool:
        return risk in self.factcheck.get("rhetoric_analysis_for", [])

    @property
    def comment_cfg(self) -> dict:
        return self.publish.get("youtube_comment", {})

    @property
    def reports_dir(self) -> Path:
        d = self.root / "reports"
        d.mkdir(exist_ok=True)
        return d

    @property
    def db_path(self) -> Path:
        return self.root / "state.db"


def load(path: str | os.PathLike | None = None) -> Config:
    root = Path(__file__).resolve().parent.parent
    cfg_path = Path(path) if path else root / "config.yaml"
    if not cfg_path.exists():
        raise SystemExit(
            f"{cfg_path} fehlt. Kopiere config.example.yaml nach config.yaml "
            f"und trage deine Kanaele ein."
        )
    raw = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}

    channels = [Channel(**c) for c in raw.get("channels", [])]
    if not channels:
        raise SystemExit("Keine Kanaele in der Konfiguration.")

    return Config(
        model=raw.get("model", "claude-opus-5"),
        lookback_hours=int(raw.get("poll", {}).get("lookback_hours", 48)),
        channels=channels,
        transcript=raw.get("transcript", {}),
        factcheck=raw.get("factcheck", {}),
        publish=raw.get("publish", {}),
        root=root,
    )
