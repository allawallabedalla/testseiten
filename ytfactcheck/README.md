# ytfactcheck

Beobachtet 3–5 YouTube-Kanäle, zieht bei jedem neuen Video das Transkript und
lässt Claude die überprüfbaren Behauptungen **mit Websuche** gegenchecken.
Bei als problematisch markierten Kanälen kommt eine Einordnung der
Argumentationsweise dazu.

```
RSS-Feed ──▶ Transkript ──▶ Behauptungen ──▶ Recherche ──▶ Urteil ──▶ Bericht
 (gratis)    (3 Stufen)      (Claude)      (Websuche)    (Claude)   ──▶ Freigabe
                                                                     ──▶ Kommentar
```

## Bevor du anfängst: zwei Dinge, die du wissen solltest

**1. Dein YouTube-Account wird zum Beobachten nicht gebraucht.**
Die Kanalüberwachung läuft über die öffentlichen RSS-Feeds
(`youtube.com/feeds/videos.xml?channel_id=UC…`) — kein API-Key, kein OAuth,
kein Quota. Der Account kommt erst ins Spiel, wenn wirklich kommentiert wird.
Häng deine Anmeldedaten auch **nicht** an das Transkript-Holen: mit
Account-Cookies zu scrapen ist genau der Weg, auf dem Accounts gesperrt werden.

**2. Automatisch gepostete Kommentare verstoßen gegen YouTubes Regeln.**
Die Spam-Richtlinien und die API Services Terms untersagen maschinell erzeugte
Kommentare. Ein Bot, der eigenständig unter fremden Videos postet, riskiert
nicht nur den API-Zugang, sondern den Google-Account. Dazu kommt der
inhaltliche Teil: „diese Aussage ist falsch“ ist unter deinem Klarnamen eine
Tatsachenbehauptung über andere Menschen — und ausgerechnet bei
kontroversen Kanälen ist ein LLM-Urteil am wenigsten verlässlich.

Deshalb ist dieses Werkzeug so gebaut, dass **du** postest und der Bot nur
vorbereitet. `post_comment()` verweigert den Dienst ohne `approved=True`, es
gibt keinen Pfad daran vorbei, und `enabled: false` ist die Voreinstellung.
Das ist kein Sicherheitsnetz, sondern die Betriebsart: recherchieren lassen,
lesen, entscheiden, posten. In der Praxis dauert die Freigabe pro Video keine
Minute — und sie ist das, was den Unterschied zwischen einem hilfreichen
Kommentar und einem automatisierten Rufschaden ausmacht.

Wenn du gar nicht posten willst, lass `enabled: false` stehen: du bekommst
dann Markdown-Berichte unter `reports/` und sonst nichts.

## Einrichten

```bash
cd ytfactcheck
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cp config.example.yaml config.yaml     # Kanäle eintragen
export ANTHROPIC_API_KEY=sk-ant-...    # oder: ant auth login
```

`yt-dlp` sollte im `PATH` liegen (`pip install yt-dlp` reicht). Der
Whisper-Fallback ist optional und braucht zusätzlich `faster-whisper` und
`ffmpeg`.

## Benutzen

```bash
python -m ytfc.cli poll      # neue Videos aus den Feeds holen
python -m ytfc.cli check     # transkribieren + faktenchecken
python -m ytfc.cli run       # beides
python -m ytfc.cli review    # Befunde durchsehen, Kommentar freigeben
python -m ytfc.cli show ID   # Bericht erneut anzeigen
python -m ytfc.cli whoami    # OAuth-Selbsttest
```

`run` läuft unbeaufsichtigt, `review` ist der Teil mit dir davor.

### Zeitplan (Linux/Raspi)

```cron
# alle 30 Minuten prüfen — review bleibt bewusst manuell
*/30 * * * * cd /pfad/zu/ytfactcheck && .venv/bin/python -m ytfc.cli run >> run.log 2>&1
```

macOS: dasselbe per `launchd` oder schlicht als Login-Item.

### Kommentieren einschalten (optional)

1. [console.cloud.google.com](https://console.cloud.google.com) → Projekt anlegen
2. **YouTube Data API v3** aktivieren
3. OAuth-Client vom Typ *Desktop-App* erstellen, JSON als
   `client_secret*.json` hier ablegen
4. In `config.yaml`: `publish.youtube_comment.enabled: true`
5. `python -m ytfc.cli whoami` → einmal im Browser bestätigen

`require_approval` und `max_per_day` bleiben aktiv. Jeder Kommentar kostet
50 Quota-Einheiten von 10.000 pro Tag — das Limit wirst du nicht sehen.

## Risikostufen

Jeder Kanal bekommt in der Config eine Stufe. Sie steuert, wie gründlich
geprüft wird:

| Stufe | Behauptungen | Aufwand | Quellen mind. | Einordnung |
|---|---|---|---|---|
| `normal` | 5 | medium | 2 | – |
| `erhoeht` | 8 | high | 3 | – |
| `problematisch` | 12 | xhigh | 3 | ja |

Bei `problematisch` läuft zusätzlich eine Analyse von Framing, Auslassungen
und Quellenumgang. Die ist ausdrücklich **kein** Faktencheck und landet nie
in einem Kommentar — sie steht nur im Bericht.

## Warum zwei getrennte Claude-Aufrufe pro Behauptung

Ein Sprachmodell, das aus dem Gedächtnis „faktencheckt“, erfindet
selbstbewusst Zahlen und kennt nichts nach seinem Trainingsstand. Deshalb:

1. **Extraktion** — Claude zieht aus dem Transkript, was sich *überhaupt*
   prüfen lässt. Meinungen, Prognosen und Wertungen fliegen raus.
2. **Recherche** — jede Behauptung einzeln, mit Websuche, ausdrücklich auch
   nach *widersprechenden* Belegen und nach Primärquellen.
3. **Urteil** — ein separater Aufruf ohne Websuche formt das
   Rechercheprotokoll in ein festes Schema. Er darf nichts ergänzen, was
   nicht im Protokoll steht.

`nicht_ueberpruefbar` ist dabei ein vollwertiges Ergebnis, kein Scheitern.
„Ich habe keinen Beleg gefunden“ ist nicht dasselbe wie „die Aussage ist
falsch“ — für *falsch* braucht es eine Quelle, die aktiv widerspricht.
Unüberprüfbare Punkte werden nie in einen Kommentar übernommen.

Das Rechercheprotokoll steht ausklappbar in jedem Bericht: du kannst jedes
Urteil bis zur Suchanfrage zurückverfolgen.

## Kosten — und warum sie hoch sind

Realistisch, mit `claude-opus-5` und heutigen Preisen:

| Stufe | pro Video |
|---|---|
| `normal` (5 Behauptungen, 5 Suchen) | ~1,60 € |
| `erhoeht` (8 Behauptungen, 6 Suchen) | ~3,20 € |
| `problematisch` (12, 8 Suchen, + Einordnung) | ~7,80 € |

Bei fünf Kanälen mit je einem Video am Tag sind das **grob 600 € im Monat**.
Das ist viel, und der Grund ist eine einzige Zahl:

```
Recherche für EINE Behauptung, 8 Suchen:
  Eingabe    82.000 Token   $0.41   ← 90 % der Kosten
  Ausgabe     6.000 Token   $0.15
  8 Suchen                  $0.08
```

82.000 Eingabe-Token für eine einzige Behauptung. Der Grund: die Websuche
läuft serverseitig in **einem** Turn, und jede Runde bekommt den bisherigen
Kontext erneut vorgelegt. Die achte Suche liest also die Ergebnisse der
ersten sieben nochmal mit. Die Eingabemenge wächst quadratisch mit der Zahl
der Suchen — und das mal zwölf Behauptungen.

Dazu zwei kleinere Posten: Denk-Token werden zum **Ausgabe**-Preis
abgerechnet (25 $/Mio.), und `xhigh` denkt viel. Websuche kostet zusätzlich
1 Cent pro Anfrage.

### Was das billiger macht

| Maßnahme | problematisch/Video | Kostet Qualität? |
|---|---|---|
| jetzt | 7,80 € | – |
| Batch-API statt Live-Aufrufen | 4,35 € | nein |
| + Urteilsschritt auf Haiku 4.5 | 4,17 € | nein |
| + `max_uses` von 8 auf 4 | 1,98 € | ja, etwas |
| + nur Behauptungen ab Relevanz 3 | 1,06 € | ja |

Die ersten beiden sind geschenkt. Der Bot läuft per Cron, es wartet niemand
auf die Antwort — die [Batch-API](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
halbiert dafür alle Token-Kosten. Und der Urteilsschritt formt nur ein
fertiges Protokoll in ein Schema; dafür braucht es kein Spitzenmodell.

Die letzten beiden nehmen Gründlichkeit weg — gerade da, wo du sie wolltest.
Wegen des quadratischen Wachstums ist `max_uses` allerdings der mit Abstand
stärkste Hebel: halb so viele Suchen kosten ein Viertel.

## Wenn keine Transkripte kommen

Läuft der Bot auf einem VPS oder in CI, blockt YouTube die
Rechenzentrums-IP meist nach wenigen Abrufen — dann liefert Stufe 1 und 2
nichts. Deshalb die Empfehlung, das Ding zuhause laufen zu lassen. Bleibt es
dabei, hilft nur `allow_whisper_fallback: true` (transkribiert die Tonspur
selbst, braucht aber CPU-Zeit und Bandbreite).

## Aufbau

| Datei | Aufgabe |
|---|---|
| `ytfc/feeds.py` | RSS-Feeds, Auflösung `@handle` → `UC…` |
| `ytfc/transcript.py` | drei Stufen: API → yt-dlp → Whisper |
| `ytfc/factcheck.py` | die Claude-Aufrufe und die Prompts |
| `ytfc/report.py` | Markdown-Bericht und Kommentartext |
| `ytfc/youtube_post.py` | OAuth und `commentThreads.insert` |
| `ytfc/state.py` | SQLite: gesehen / geprüft / gepostet |
| `ytfc/cli.py` | die Unterbefehle |
