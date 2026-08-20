"""Neue Videos finden — ueber die oeffentlichen RSS-Feeds von YouTube.

Bewusst ohne YouTube Data API: der Feed
``https://www.youtube.com/feeds/videos.xml?channel_id=UC...``
ist frei abrufbar, braucht weder API-Key noch OAuth und kostet kein Quota.
Er liefert die letzten ~15 Videos eines Kanals.
"""

from __future__ import annotations

import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

FEED_URL = "https://www.youtube.com/feeds/videos.xml?channel_id={cid}"
UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0 Safari/537.36"
)
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}
_CHANNEL_ID_RE = re.compile(r'"(?:channelId|externalId)":"(UC[\w-]{22})"')


def _get(url: str, timeout: int = 20) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def resolve_channel_id(handle: str) -> str:
    """@handle -> UC...-ID, indem die Kanalseite gelesen wird.

    Die ID steht als ``"channelId":"UC..."`` im ausgelieferten HTML. Das
    braucht keinen API-Key; wenn YouTube das Markup aendert, faellt es hier
    mit einer klaren Meldung auf statt still das Falsche zu tun.
    """
    slug = handle if handle.startswith("@") else f"@{handle}"
    html = _get(f"https://www.youtube.com/{slug}")
    m = _CHANNEL_ID_RE.search(html)
    if not m:
        raise RuntimeError(
            f"Channel-ID fuer {slug} nicht gefunden. Trage sie in der Config "
            f"direkt als channel_id: UC... ein."
        )
    return m.group(1)


def fetch_feed(channel_id: str) -> list[dict]:
    """Alle Eintraege des Kanal-Feeds als Dicts."""
    xml = _get(FEED_URL.format(cid=channel_id))
    root = ET.fromstring(xml)
    entries = []
    for e in root.findall("atom:entry", NS):
        vid = e.findtext("yt:videoId", namespaces=NS)
        title = e.findtext("atom:title", namespaces=NS)
        published = e.findtext("atom:published", namespaces=NS)
        if not (vid and title and published):
            continue
        entries.append(
            {
                "video_id": vid,
                "title": title.strip(),
                "published": published,
                "url": f"https://www.youtube.com/watch?v={vid}",
            }
        )
    return entries


def recent(entries: list[dict], lookback_hours: int) -> list[dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    out = []
    for e in entries:
        try:
            ts = datetime.fromisoformat(e["published"].replace("Z", "+00:00"))
        except ValueError:
            continue
        if ts >= cutoff:
            out.append(e)
    return out
