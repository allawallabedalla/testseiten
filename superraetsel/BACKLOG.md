# SuperRätsel — Backlog

Priorisiert nach Nutzerwert und technischer Abhängigkeit. Jede Aufgabe nennt das
kosteneffizienteste Claude-Modell für die Umsetzung:

| Modell | Einsatz |
|---|---|
| **Haiku 4.5** | Mechanische Änderungen: CSS-Feinschliff, Texte, Listen erweitern |
| **Sonnet 5** | Standard-Featurearbeit: Layout, Refactoring, Frontend-Logik |
| **Opus 5 / Fable 5** | Architektur-Entscheidungen, Backend, Sicherheit, komplexe Algorithmen |

Faustregel: Design/Architektur einmalig mit dem großen Modell klären, die
Umsetzung dann in kleine Pakete schneiden, die Sonnet oder Haiku abarbeiten.

---

## P0 — Als Nächstes (vom Nutzer gefordert)

### 1. Flat-White-Design
**Modell: Sonnet 5** (einmaliges Redesign), Feinschliff danach mit Haiku 4.5
- Komplettes Restyling: weißer Grund, flache Flächen, keine Schatten/Verläufe,
  keine 3D-Optik. Der bisherige „Papier"-Look (Beige, Verläufe im Logo,
  Schlagschatten) wird ersetzt.
- Emojis (🔥🧊💡🥇🧰 …) durch flache Inline-SVG-Icons oder typografische
  Zeichen ersetzen — nirgends 3D-/Plattform-Emojis.
- Dark Mode = echte Invertierung des Flat-White-Looks (schwarzer Grund,
  weiße Linien), kein eigenes zweites Farbschema.
- Akzeptanz: keine `box-shadow`, keine `linear-gradient`, kein Emoji im UI;
  Kontrast in beiden Modi ≥ WCAG AA.

### 2. iPhone-Optimierung
**Modell: Sonnet 5**, Kleinteile (Meta-Tags, Copy) mit Haiku 4.5
- Safe-Area-Insets (Notch/Home-Indicator), `viewport-fit=cover`.
- Touch-Ziele ≥ 44×44 pt (Schiebepuzzle-Felder, Ziffernfelder, Buttons).
- iOS-Tastatur: kein Auto-Zoom bei Input-Fokus (Schriftgröße ≥ 16px),
  passende `inputmode`/`autocapitalize`/`enterkeyhint`-Attribute.
- Kein Layout-Springen, wenn die Tastatur aufgeht (Wortle-Eingabe).
- Web-App-Meta-Tags für „Zum Home-Bildschirm": Icon, Titel, Statusbar-Stil.
- Test auf 375px-Breite (iPhone SE) bis 430px (Pro Max).

### 3. Geräteübergreifende Rangliste
**Modell: Fable 5 / Opus 5** für Architektur & Sicherheit, Umsetzung Sonnet 5
- Entscheidung nötig (Architektur-Task): gehostetes BaaS (Supabase/Firebase,
  kostenloser Tier reicht) vs. eigene Mini-API. Statische Seite bleibt erhalten.
- Name bleibt der einzige Login — dafür braucht es ein Konzept gegen
  Namens-Kollisionen (z. B. Name + kurzer selbstgewählter PIN oder
  Gerätetoken, das den Namen „besitzt").
- Score-Submission absichern (Plausibilitätsprüfung serverseitig: max. 4
  Rätsel/Tag, Score ≤ 100 — sonst trägt jeder 999999 ein).
- Offline-Fallback: ohne Netz weiter lokal spielen, Sync bei Reconnect.
- Akzeptanz: zwei Geräte sehen dieselbe Rangliste; Ausfall des Backends
  bricht das Spiel nicht.

---

## P1 — Danach (stabilisiert das Tagesgeschäft)

### 4. Tageszustand überlebt Reload
**Modell: Sonnet 5**
- Gelöste Rätsel, Wortle-Versuche und Zugzahlen des Tages in localStorage
  halten; nach Reload ist der Tag nicht „zurückgesetzt" (verhindert auch
  Mehrfach-Punkte durch Neuladen — Voraussetzung für faire Rangliste, daher
  vor/mit Aufgabe 3 umsetzen).

### 5. Wortliste & Rätselpool ausbauen
**Modell: Haiku 4.5**
- Wortle: von 25 auf ≥ 365 kuratierte deutsche 5-Buchstaben-Wörter
  (keine Beugungen, keine Namen); optional Gültigkeits-Wörterbuch für Eingaben.
- Escape-Rätsel: von 6 auf ≥ 60 Rätsel, damit sich der Pool nicht alle
  Woche wiederholt.
- Herkunfts-Fakten variieren (mehrere pro Kategorie, täglich wechselnd).

### 6. Teilbares Ergebnis-Raster verbessern
**Modell: Haiku 4.5**
- Ein gemeinsames Tages-Share (alle 4 Ergebnisse in einem Block) statt
  vier einzelner; Web Share API auf iOS (`navigator.share`) statt nur
  Zwischenablage. Flat-Design-konforme Zeichen statt Emojis prüfen —
  im Share-Text sind Emojis ok (Wordle-Konvention).

### 7. PWA: Installierbar + offline
**Modell: Sonnet 5**
- Manifest + Service Worker; die App läuft vom Home-Bildschirm wie nativ
  (baut auf Aufgabe 2 auf).

---

## P2 — Später (Wachstum & Tiefe)

### 8. Archiv mit Tipp-Token
**Modell: Sonnet 5**
- Verpasste Tagesausgaben gegen Token nachspielen (zählt nicht für Serie,
  wohl aber fürs Stärken-Profil).

### 9. RQ-Kalibrierung
**Modell: Fable 5 / Opus 5** (Konzept), Sonnet 5 (Umsetzung)
- Score-Formeln pro Kategorie gegen echte Spieldaten prüfen (ist das
  Schiebepuzzle-Par fair? Sind 5 Rätsel als Minimum genug?); RQ ggf. mit
  Konfidenzangabe („± 10") ehrlicher machen.

### 10. Freunde-Vergleich
**Modell: Sonnet 5** (braucht Aufgabe 3)
- Private Ranglisten per teilbarem Gruppen-Link statt globaler Liste —
  Motivation kommt vom Vergleich mit Bekannten, nicht mit Fremden.

### 11. Wochen-Challenge / Saisonevents
**Modell: Sonnet 5**
- Wöchentlich ein Sonderrätsel mit doppelten Punkten; Saisonabschluss
  archiviert die Rangliste und startet eine neue Runde (verhindert
  uneinholbare Dauerspitzenreiter).

---

## Erledigt

- ✅ Recherche erfolgreichste Rätsel & Apps, Fusionskonzept (Fable 5)
- ✅ Vier spielbare Kategorien mit täglicher Inhalts-Rotation (Fable 5)
- ✅ Namens-Login, lokale Rangliste, Punkte (Fable 5)
- ✅ Streaks mit Freeze-Token, Tipp-Token, perfekter Tag (Fable 5)
- ✅ Stärken-Profil + RQ-Schätzung mit Disclaimer (Fable 5)
