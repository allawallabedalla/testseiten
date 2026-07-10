# EchtGetestet 🔍✓

**Finde echte Produkttests statt Fake-Reviews und Affiliate-Fallen.**

Google liefert bei Suchen wie „Akkuschrauber Test" häufig Seiten, die nie ein
Produkt in der Hand hatten – automatisch generierte „Vergleiche" mit
Amazon-Affiliate-Links. Diese Website löst das Problem, indem sie **gar nicht
erst im offenen Web sucht**, sondern ausschließlich eine kuratierte Whitelist
unabhängiger Testportale abfragt – und die besten Treffer direkt anzeigt.

## Wie es funktioniert

1. **Produkt eingeben, Knopf drücken** – mehr Bedienung gibt es nicht.
2. Die Kategorie wird automatisch erkannt (Schlagwort-Matching), passende
   Portale werden ausgewählt.
3. Die Seite ruft die Suchergebnisse der Portale ab (DuckDuckGo mit
   `site:`-Filter, über öffentliche CORS-Proxys, da eine statische Seite
   Suchmaschinen nicht direkt abfragen darf).
4. Die Treffer erscheinen **direkt auf der Seite**, sortiert nach:
   - **Reputation** der Quelle (Unabhängigkeit, Methodik, Labor; 1–10)
   - **Zugänglichkeit** (frei lesbare Tests vor Paywall-Inhalten)
   - Sprache (Deutsch leicht bevorzugt) und Relevanz des Titels
5. Zu jedem Treffer gibt es ein **Kurzfazit** (Auszug aus dem Testbericht)
   und den direkten Link zum vollständigen Test.

Sind die CORS-Proxys nicht erreichbar, fällt die Seite automatisch auf
direkte Suchlinks zurück – die Suche funktioniert also immer.

## Community-Konsens von Reddit

Parallel zur Portalsuche wertet die Seite Reddit-Diskussionen aus – ganz
ohne LLM:

1. Passende Threads werden über Reddits JSON-API gesucht (die erlaubt
   direkte Browser-Aufrufe, Proxys nur als Fallback).
2. Aus den Top-Kommentaren der besten Threads werden **Produktnennungen
   extrahiert und upvote-gewichtet gezählt** (Heuristik: Eigennamen und
   Modellnummern; Stopwörter, generische Begriffe und das Suchwort selbst
   werden gefiltert, „Roborock" geht in „Roborock S8" auf).
3. Angezeigt werden die meistgenannten Produkte, die meist-upvoteten
   Zitate und die ausgewerteten Threads mit Links.

Das ist bewusst als „gewichtetes Stimmungsbild" gekennzeichnet – kein
Labortest, aber ehrliche Erfahrungen echter Nutzer:innen.

Zusätzlich enthält die Seite eine Checkliste, wie man Fake-Tests in
30 Sekunden selbst erkennt.

## Aufnahmekriterien für die Whitelist

Ein Portal wird nur aufgenommen, wenn es:

- **selbst testet** – im Labor, mit Messwerten oder in echter redaktioneller Praxis
- eine **nachvollziehbare Methodik** offenlegt
- **kein reines Affiliate-Geschäftsmodell** hat
- auch **negative Urteile** veröffentlicht

Aktuell dabei u. a.: Stiftung Warentest, ÖKO-TEST, Konsument (AT), K-Tipp (CH),
ADAC, RTINGS, Notebookcheck, heise/c't, ComputerBase, AV-TEST, DXOMARK,
Consumer Reports, Which?, OutdoorGearLab, RunRepeat, medizin-transparent.

Fehlt ein seriöses Portal? → Issue aufmachen oder PR mit Ergänzung in der
`SITES`-Liste in `index.html` stellen (Reputation `rep` und Zugänglichkeit
`access` mit angeben).

## Technik

- Eine einzige `index.html` – kein Build, kein Backend, keine Cookies, kein Tracking
- Design im **Neumorphism-Stil** (Soft UI), Hell-/Dunkelmodus folgt der Systemeinstellung
- Ergebnis-Abruf clientseitig über öffentliche CORS-Proxys
  (`corsproxy.io`, `allorigins.win` raw+get, `codetabs.com` – der Reihe nach
  probiert), zusätzlich Bing-Ergebnisse über den Jina-Reader (`r.jina.ai`)
  als zweiter Suchweg, falls DuckDuckGo die Proxy-IPs blockt
- Läuft direkt über GitHub Pages oder jeden statischen Webserver

> **Hinweis:** Öffentliche CORS-Proxys sind ein Kompromiss – sie können
> rate-limitiert oder zeitweise offline sein. Für einen zuverlässigeren
> Betrieb kann man denselben Abruf in einen eigenen Cloudflare Worker o. ä.
> auslagern und die `PROXIES`-Liste in `index.html` darauf zeigen lassen.

### Lokal ansehen

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

### Mit GitHub Pages veröffentlichen

Repo-Einstellungen → **Pages** → Source: Branch auswählen, Ordner `/ (root)` → Save.
Die Seite ist danach unter `https://<user>.github.io/testseiten/` erreichbar.

## Lizenz

Frei nutzbar (MIT). Keine Affiliate-Links, keine Werbung.
