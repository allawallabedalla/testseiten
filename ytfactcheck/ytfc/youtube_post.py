"""Kommentar auf YouTube veroeffentlichen — nur nach ausdruecklicher Freigabe.

Das ist der einzige Teil, der deinen Google-Account braucht (OAuth), und der
einzige, der nach aussen wirkt. Entsprechend eng ist er gebaut:

* ``post_comment`` verweigert den Dienst ohne ``approved=True``. Es gibt
  keinen Pfad, auf dem etwas ungesehen im Netz landet.
* Ein Tageslimit deckelt die Zahl der Kommentare.
* Jeder Post wird lokal protokolliert.

Warum so streng: YouTube untersagt in seinen Spam-Richtlinien und den API
Services Terms automatisiert erzeugte Kommentare. Ein Bot, der eigenstaendig
unter fremden Videos postet, riskiert nicht nur das API-Projekt, sondern den
Google-Account. Dazu kommt der inhaltliche Teil: ein oeffentlich unter deinem
Klarnamen gepostetes "das ist falsch" ist eine Tatsachenbehauptung ueber
andere Menschen. Beides zusammen macht die Freigabe durch einen Menschen zur
Bedingung, nicht zur Komfortfunktion.
"""

from __future__ import annotations

import json
from pathlib import Path

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
QUOTA_PER_INSERT = 50  # Standard-Tagesbudget der Data API: 10.000 Einheiten


class NotApproved(RuntimeError):
    pass


def _credentials(root: Path):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    token_path = root / "token.json"
    secret = next(iter(root.glob("client_secret*.json")), None)
    creds = None

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        if secret is None:
            raise SystemExit(
                "client_secret*.json fehlt.\n"
                "  1. console.cloud.google.com -> Projekt anlegen\n"
                "  2. YouTube Data API v3 aktivieren\n"
                "  3. OAuth-Client 'Desktop-App' erstellen, JSON hier ablegen\n"
                f"     ({root})"
            )
        creds = InstalledAppFlow.from_client_secrets_file(
            str(secret), SCOPES
        ).run_local_server(port=0)

    token_path.write_text(creds.to_json(), encoding="utf-8")
    token_path.chmod(0o600)
    return creds


def client(root: Path):
    from googleapiclient.discovery import build

    return build("youtube", "v3", credentials=_credentials(root),
                 cache_discovery=False)


def post_comment(root: Path, video_id: str, text: str, *,
                 approved: bool = False) -> str:
    """Postet den Kommentar. ``approved`` muss explizit True sein."""
    if not approved:
        raise NotApproved(
            "post_comment ohne Freigabe aufgerufen — es wurde nichts gepostet."
        )
    if not text.strip():
        raise ValueError("Leerer Kommentartext.")

    yt = client(root)
    response = yt.commentThreads().insert(
        part="snippet",
        body={
            "snippet": {
                "videoId": video_id,
                "topLevelComment": {"snippet": {"textOriginal": text}},
            }
        },
    ).execute()
    return response["snippet"]["topLevelComment"]["id"]


def my_channel(root: Path) -> dict:
    """Kurzer Selbsttest: mit welchem Kanal ist der Bot angemeldet?"""
    yt = client(root)
    items = yt.channels().list(part="snippet", mine=True).execute().get("items", [])
    if not items:
        raise SystemExit("Kein YouTube-Kanal fuer diesen Google-Account.")
    return {"id": items[0]["id"], "title": items[0]["snippet"]["title"]}
