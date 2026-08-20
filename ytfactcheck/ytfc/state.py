"""SQLite-State: welche Videos gesehen, geprueft und kommentiert wurden."""

from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from datetime import date
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS channels (
    channel_id TEXT PRIMARY KEY,
    handle     TEXT,
    name       TEXT
);
CREATE TABLE IF NOT EXISTS videos (
    video_id     TEXT PRIMARY KEY,
    channel_id   TEXT NOT NULL,
    channel_name TEXT NOT NULL,
    risk         TEXT NOT NULL,
    title        TEXT NOT NULL,
    published    TEXT NOT NULL,
    seen_at      TEXT NOT NULL DEFAULT (datetime('now')),
    status       TEXT NOT NULL DEFAULT 'neu',
    note         TEXT
);
CREATE TABLE IF NOT EXISTS reports (
    video_id   TEXT PRIMARY KEY REFERENCES videos(video_id),
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    payload    TEXT NOT NULL,
    md_path    TEXT
);
CREATE TABLE IF NOT EXISTS posts (
    video_id   TEXT PRIMARY KEY REFERENCES videos(video_id),
    posted_at  TEXT NOT NULL DEFAULT (datetime('now')),
    comment_id TEXT,
    body       TEXT NOT NULL
);
"""

# 'neu' -> 'geprueft' -> 'gepostet'; Sackgassen: 'kein_transkript', 'fehler',
# 'nichts_zu_melden' (geprueft, aber kein Befund der einen Kommentar rechtfertigt)
STATUS_NEW = "neu"
STATUS_CHECKED = "geprueft"
STATUS_POSTED = "gepostet"
STATUS_NO_TRANSCRIPT = "kein_transkript"
STATUS_CLEAN = "nichts_zu_melden"
STATUS_ERROR = "fehler"


class State:
    def __init__(self, path: Path):
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.executescript(SCHEMA)
        self.db.commit()

    @contextmanager
    def _tx(self):
        try:
            yield self.db
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise

    # --- Kanaele ----------------------------------------------------------

    def cached_channel_id(self, handle: str) -> str | None:
        row = self.db.execute(
            "SELECT channel_id FROM channels WHERE handle = ?", (handle,)
        ).fetchone()
        return row["channel_id"] if row else None

    def remember_channel(self, channel_id: str, handle: str | None, name: str) -> None:
        with self._tx() as db:
            db.execute(
                "INSERT OR REPLACE INTO channels(channel_id, handle, name) "
                "VALUES (?, ?, ?)",
                (channel_id, handle, name),
            )

    # --- Videos -----------------------------------------------------------

    def is_known(self, video_id: str) -> bool:
        return (
            self.db.execute(
                "SELECT 1 FROM videos WHERE video_id = ?", (video_id,)
            ).fetchone()
            is not None
        )

    def add_video(self, video: dict) -> None:
        with self._tx() as db:
            db.execute(
                "INSERT OR IGNORE INTO videos"
                "(video_id, channel_id, channel_name, risk, title, published) "
                "VALUES (:video_id, :channel_id, :channel_name, :risk, :title,"
                " :published)",
                video,
            )

    def set_status(self, video_id: str, status: str, note: str | None = None) -> None:
        with self._tx() as db:
            db.execute(
                "UPDATE videos SET status = ?, note = ? WHERE video_id = ?",
                (status, note, video_id),
            )

    def pending(self, status: str = STATUS_NEW, limit: int = 50) -> list[sqlite3.Row]:
        return list(
            self.db.execute(
                "SELECT * FROM videos WHERE status = ? ORDER BY published DESC "
                "LIMIT ?",
                (status, limit),
            )
        )

    def video(self, video_id: str) -> sqlite3.Row | None:
        return self.db.execute(
            "SELECT * FROM videos WHERE video_id = ?", (video_id,)
        ).fetchone()

    # --- Berichte ---------------------------------------------------------

    def save_report(self, video_id: str, payload: dict, md_path: str) -> None:
        with self._tx() as db:
            db.execute(
                "INSERT OR REPLACE INTO reports(video_id, payload, md_path) "
                "VALUES (?, ?, ?)",
                (video_id, json.dumps(payload, ensure_ascii=False), md_path),
            )

    def report(self, video_id: str) -> dict | None:
        row = self.db.execute(
            "SELECT payload FROM reports WHERE video_id = ?", (video_id,)
        ).fetchone()
        return json.loads(row["payload"]) if row else None

    # --- Posts ------------------------------------------------------------

    def posts_today(self) -> int:
        row = self.db.execute(
            "SELECT COUNT(*) AS n FROM posts WHERE date(posted_at) = ?",
            (date.today().isoformat(),),
        ).fetchone()
        return int(row["n"])

    def record_post(self, video_id: str, comment_id: str | None, body: str) -> None:
        with self._tx() as db:
            db.execute(
                "INSERT OR REPLACE INTO posts(video_id, comment_id, body) "
                "VALUES (?, ?, ?)",
                (video_id, comment_id, body),
            )
