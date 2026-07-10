# EchtGetestet 🔍✓

**Finde echte Produkttests statt Fake-Reviews und Affiliate-Fallen.**

Google liefert bei Suchen wie „Akkuschrauber Test" häufig Seiten, die nie ein
Produkt in der Hand hatten – automatisch generierte „Vergleiche" mit
Amazon-Affiliate-Links. Diese Website löst das Problem, indem sie **gar nicht
erst im offenen Web sucht**, sondern gezielt eine kuratierte Whitelist
unabhängiger Testportale durchsucht.

## Wie es funktioniert

1. **Produkt eingeben** (z. B. „Saugroboter", „Kindersitz", „OLED Fernseher")
2. Die Kategorie wird automatisch erkannt (per Schlagwort-Matching) oder manuell gewählt
3. Zu jedem passenden Testportal gibt es einen Suchlink mit `site:`-Filter –
   so tauchen Fake-Seiten in den Ergebnissen gar nicht erst auf
4. Die **Meta-Suche** durchsucht bis zu 8 Portale der Kategorie gleichzeitig
   (`produkt test (site:test.de OR site:oekotest.de OR …)`)
5. Die Suchmaschine ist wählbar (DuckDuckGo, Startpage, Ecosia, Google, Bing)

Zusätzlich enthält die Seite eine Checkliste, wie man Fake-Tests in 30 Sekunden
selbst erkennt.

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
`SITES`-Liste in `index.html` stellen.

## Technik

- Eine einzige `index.html` – kein Build, kein Backend, keine Cookies, kein Tracking
- Läuft direkt über GitHub Pages oder jeden statischen Webserver
- Hell-/Dunkelmodus folgt der Systemeinstellung

### Lokal ansehen

```bash
# Datei einfach im Browser öffnen, oder:
python3 -m http.server 8000
# → http://localhost:8000
```

### Mit GitHub Pages veröffentlichen

Repo-Einstellungen → **Pages** → Source: Branch auswählen, Ordner `/ (root)` → Save.
Die Seite ist danach unter `https://<user>.github.io/testseiten/` erreichbar.

## Lizenz

Frei nutzbar (MIT). Keine Affiliate-Links, keine Werbung.
