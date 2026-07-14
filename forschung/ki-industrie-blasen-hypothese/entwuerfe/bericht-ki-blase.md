<!--
Provenienz: Erstellt am 2026-07-14 in einem interdisziplinaeren Multi-Agent-Rechercheprozess
(Lead-Analyst + 6 Analyse-Referate mit Live-Websuche + Erstautor + adversarialer Faktencheck).
Methodik, datierte Rohbefunde und Faktencheck-Protokoll: ../daten/evidenz-methodik-appendix.md.
Hinweis: Aussagen ueber aktuelle Ereignisse/Zahlen/Zitate sind quellennah recherchiert und
stichprobenartig gegen die Berichterstattung geprueft; vor Verwendung unabhaengig verifizieren.
Keine Anlageberatung.
-->

# Rechnen KI-Firmen selbst mit dem Platzen der Blase? Eine Prüfung der Signale 2024–2026

## Executive Summary

**Urteil (kalibriert):** Die Kernhypothese – KI-Firmen antizipieren *intern* einen Crash und richten Handeln *und* Kommunikation defensiv danach aus – ist in ihrer **starken Lesart überwiegend nicht gestützt**. In einer **schwachen Lesart** – Akteure erkennen eine Überhitzung und realisieren Buchgewinne, solange das Bewertungsfenster offen ist – ist sie **teilweise gestützt**, nach Bereinigung um Confounder aber nur schwach. **Gesamtkonfidenz: mittel.**

Der Befund spaltet sich entlang zweier Achsen. Erstens **Worte gegen Taten**: Auf der Ebene öffentlicher Aussagen räumen führende Akteure – Altman, Zuckerberg, Pichai, Hassabis, Amodei – zwischen August und November 2025 wörtlich eine Blase oder „Irrationalität" ein. Das ist der belastbarste Pro-Teil. Ihre dominante *revealed preference* ist jedoch massives Doubling-down: Rekord-Capex von rund 725 Mrd. USD für 2026 (+77 %), mehrjährige, teils nicht stornierbare Compute-Verpflichtungen bis 2031, laufende Mega-Finanzierungsrunden. Wer intern einen nahen Crash einpreist, bindet nicht hunderte Milliarden in abschreibungsintensive Assets.

Zweitens **differieren die Akteure**: Bereits börsennotierte oder periphere Beteiligte monetarisieren aggressiv (CoreWeave-Gründer über 2,3 Mrd. USD, Großinvestor Magnetar über 5,5 Mrd. USD, Chip-Insider bei Nvidia/Palantir/Broadcom rund 4,6 Mrd. USD), während Insider der strategischen Kernlabore eher *halten* (Anthropics Tender blieb unterzeichnet, weil zu wenige Mitarbeiter verkaufen wollten). Entscheidend: Die stärksten Cash-out-Signale werden durch vorab terminierte 10b5-1-Pläne, erstmalige Post-Lock-up-Liquidität, Diversifikation und regulatorische Confounder erheblich entkräftet – sie liefern keinen sauberen Beleg für eine *Crash-Erwartung*.

**Die drei stärksten Signale FÜR die Hypothese (mit Vorbehalt gelesen):** (1) die wörtlichen Blasen-Eingeständnisse der Kernakteure selbst – das einzige Signal, das *direkt* auf eine antizipierte Korrektur zeigt; (2) das breite Insider- und Frühinvestoren-Cash-out bei Höchstbewertungen – *nur schwach*, weil durch 10b5-1-Automatik, Diversifikation und Lock-up-Mechanik konfundiert und überwiegend an der Peripherie, nicht in den Kernlaboren, verortet; (3) punktuelle Bilanz-Vorsicht (Amazon-Abschreibungsverkürzung, Microsoft-Lease-Stornierungen) – *ambivalent*, weil ebenso als Risikomanagement bei fortgesetztem Ausbau lesbar. Die zeitliche Koinzidenz der Mega-IPO-Welle 2026 mit einer hohen CAPE-Bewertung wird hier bewusst **nicht** als Verhaltensbeleg geführt: Sie ist ein Makro-/Kontextindikator, kein Nachweis firmeninterner Crash-Erwartung.

**Die drei stärksten Signale GEGEN die Hypothese:** (1) das beschleunigte Doubling-down beim Capex als dominante *revealed preference*; (2) Kernlab-Insider, die halten statt auszusteigen; (3) real und stark beschleunigende, zahlungswirksame Nachfrage (Nvidia Data-Center +92 % YoY, Microsoft-Backlog rund 625 Mrd. USD, Token-Volumen 7× YoY laut Sekundärberichten).

---

## 1. Einleitung und Operationalisierung der Hypothese

Die Ausgangsfrage lautet nicht, ob 2024–2026 *objektiv* eine KI-Blase besteht – das ist eine getrennt gehaltene **Kontextfrage** (Abschnitt 8). Getestet wird die enger gefasste **Verhaltenshypothese**: Rechnen die Akteure – Gründer, Führungskräfte, Frühinvestoren der strategischen KI-Kernlabore – selbst mit einer signifikanten Bewertungskorrektur und richten Verhalten und Kommunikation danach aus?

Zur Prüfung trenne ich zwei Evidenzklassen:

- **Revealed Preferences** – aus tatsächlichem Handeln abgeleitete Erwartungen: Timing und Struktur von Börsengängen, Insiderverkäufe, Lock-up-Design, Downside-Klauseln, Verschuldungsstruktur, Diversifikation, Hedging.
- **Stated Preferences** – explizite öffentliche Aussagen zu Blase oder Korrektur.

**Beweisstandard:** Bei Konflikt zwischen beiden erhalten *revealed preferences* höheres Gewicht, weil Aussagen strategisch oder „talking the book" sein können. Die Hypothese gilt als **widerlegt**, wenn Verhalten und Aussagen überwiegend auf fortgesetztes Commitment und Crash-Ignoranz deuten; als **gestützt**, wenn beobachtbares Handeln (Cash-out-Timing, Absicherung, Risikoexternalisierung) und Kommunikation kohärent auf eine antizipierte Korrektur hinweisen.

**Zwei Confounder-Grundsätze vorab.** Erstens: Ein Verhaltenssignal zählt nur dann als Crash-Beleg, wenn es sich nicht ebenso gut durch marktunabhängige Mechanik erklären lässt (vorab terminierte Verkaufspläne, erstmalige Liquidität nach Lock-up, Diversifikation aus Klumpenrisiko, Optionsvergütungs-Base-Rates). Zweitens: Ein Signal muss den *richtigen Akteuren* zurechenbar sein. Verkäufe börsennotierter Chip- oder Analytics-Firmen (Nvidia, Palantir, Broadcom) sagen wenig über die *interne* Crash-Erwartung der strategischen Kernlabore (OpenAI, Anthropic) aus – die Zurechnung „Peripherie verkauft" → „die Firmen erwarten Crash" ist eine Attributions-Rutschbahn, die ich ausdrücklich vermeide.

**Grundlegende Limitation vorab:** Es liegen keine internen Dokumente oder Board-Kommunikationen vor, die zeigen, ob Firmen intern einen Crash modellieren. Alle Signale sind extern beobachtetes Verhalten oder öffentliche Aussagen. Jede Aussage über „interne Erwartungen" ist damit eine *Inferenz*, kein direkter Beleg.

---

## 2. Indikator A – IPO-Timing und Cash-out

### Belege für Fensterausnutzung

Das handfesteste Pro-Material liefert das Cash-out-Verhalten bereits liquider Akteure. Die drei CoreWeave-Mitgründer Michael Intrator, Brannin McBee und Brian Venturo verkauften seit Ablauf der Lock-up-Frist im August 2025 zusammen über 2,3 Mrd. USD eigener Aktien; Chief Strategy Officer Venturo allein über 1,1 Mrd. USD (Bloomberg, 09.06.2026). Der Großinvestor Magnetar Financial halbierte seinen Anteil auf 9,7 % und veräußerte über 5,5 Mrd. USD – deutlich mehr als die Gründer (Bloomberg/Crain's Chicago Business, 09.06.2026). Aggregiert nennt MarketBeat rund 8,5 Mrd. USD Insiderverkäufe bei CoreWeave binnen zwölf Monaten, mit dem Rekordquartal Q2 2026 (3,27 Mrd. USD) (Yahoo Finance/MarketBeat, 12.07.2026).

Bei den privaten Kernlaboren zeigt sich vorzeitige Liquidität in historisch außergewöhnlichem Umfang: OpenAI-Mitarbeiter verkauften im Oktober 2025 6,6 Mrd. USD bei 500 Mrd. USD Bewertung, wobei rund 75 Beschäftigte das Verkaufslimit von 30 Mio. USD voll ausschöpften (CNBC, 02.10.2025). The Information beziffert das kumulierte Mitarbeiter-Cash-out bei OpenAI und Anthropik vor einem Börsengang auf rund 14 Mrd. USD (The Information, gemeldet Anfang 2026; **unbestätigt – Paywall-Sekundärzitat, Methodik nicht offengelegt; nicht als harte Basis der „breites Cash-out"-These verwendet**). Hinzu kommt xAIs 300-Mio.-USD-Tender bei 113 Mrd. USD Bewertung (TechCrunch/FT, 02.06.2025).

Zeitlich fällt eine konzentrierte Mega-IPO-Welle 2026 mit expliziten Blasen-Warnungen zusammen: Anthropic reichte am 01.06.2026 einen Draft-S-1 bei rund 965 Mrd. USD ein, OpenAI am 08.06.2026 mit Ziel rund 1 Bio. USD, SpaceX (inklusive xAI) folgte am 12.06.2026 – zeitgleich mit einer CAPE-Ratio über 40 und Warnungen von Bank of England, Dimon und Dalio (Fortune, 08.06.2026). **Einordnung:** Ein CAPE über 40 wurde historisch bislang nur zweimal erreicht – 1999/2000 vor dem Dotcom-Crash und erneut ab 2021; die Marke ist außergewöhnlich, aber nicht einmalig. Wichtiger noch: Sie ist ein *Makro-/Kontextindikator*. Dass IPOs in ein Hochbewertungsfenster fallen, ist per se **kein Beleg** für eine firmeninterne Crash-Erwartung – Börsengänge in Hochbewertungsphasen sind der Normalfall und ökonomisch rational, unabhängig von der Blasenmeinung der Emittenten. Ich führe diese Koinzidenz daher als Kontext, nicht als Verhaltenssignal.

### Belege dagegen

Mehrere gewichtige Fakten sprechen gegen die *starke* Lesart. Erstens war CoreWeaves IPO im März 2025 **verkleinert und unter der Preisspanne** platziert – 40 USD statt der erwarteten 47–55 USD, Volumen von 49 auf 37,5 Mio. Aktien gekürzt, Erlös überwiegend Primärkapital für die Firma (CNBC, 27.03.2025). Das ist schwache, keine gierige Nachfrage – das Gegenteil eines gedrängten Timings.

Zweitens – und am stärksten – blieb **Anthropics Tender im April 2026 unterzeichnet, weil Mitarbeiter hielten**: Investoren konnten nicht die geplante Menge kaufen, da zu wenige verkaufen wollten – nicht aus Unzufriedenheit mit dem Preis, sondern weil viele auf höhere künftige Werte wetteten (Bloomberg, 08.04.2026). Anthropic verhängte zudem seit mindestens Februar 2026 aktive Transfer-Restriktionen (TechCrunch, 28.05.2026). Das ist ein starkes gegenläufiges *revealed-preference*-Signal – und es betrifft ein Kernlabor, also genau den Akteurstyp, um den die Hypothese kreist.

Drittens laufen die Gründerverkäufe über **vorab terminierte 10b5-1-Pläne**, die Monate im Voraus fixiert werden. Zwei weitere mechanische Confounder verstärken die Entkräftung: (a) Die Verkäufe setzen unmittelbar nach **Lock-up-Ablauf** ein – erste Liquidität nach dem IPO ist bei Gründern erwartbar, unabhängig von der Marktmeinung; (b) bei Gründern mit über 90 % Vermögenskonzentration in einer einzelnen, zuvor illiquiden Aktie ist Diversifikation ökonomisch geboten, auch ohne Crash-Erwartung. Entscheidend ist zudem das **Verhältnis von verkauft zu gehalten**: Die CoreWeave-Gründer halten trotz Verkäufen noch rund 18 % – ein Anteil, der die verkauften 2,3 Mrd. USD deutlich übersteigt. Wer einen Crash einpreist, hält nicht den Löwenanteil seines Vermögens in der Aktie. Das Verhältnis verkauft-zu-gehalten ist damit selbst ein *Gegen*argument, kein Pro-Signal (Seeking Alpha, 09.06.2026).

Viertens ist der dominant *erklärte* Grund für Börsengänge der gigantische Capex-Bedarf, nicht Insider-Ausstieg: JPMorgan projiziert 5,5 Bio. USD globalen KI-Capex bis 2030, OpenAI plant Rechenzentren in der Größenordnung mehrerer hundert Milliarden USD (Bloomberg, 06.05.2026). Cerebras' IPO-Verzögerung war zudem regulatorisch getrieben (CFIUS-Prüfung wegen G42), nicht markt-timing-getrieben (Tech Startups, 19.12.2025).

**Zwischenfazit A:** Das Verhalten belegt breites Realisieren von Buchgewinnen bei Hochbewertung („Chips vom Tisch nehmen"), stützt also die schwache Lesart. Nach Abzug der Confounder (10b5-1, Lock-up-Mechanik, Diversifikation) und angesichts der hohen Halte-Quoten bleibt das Netto-Signal jedoch schwach. Es belegt nicht, dass die Firmen selbst mit einem Platzen rechnen – bei den Kernlaboren zeigen Insider teils das Gegenteil.

---

## 3. Indikator B – Lab-Finanzierung und zirkuläre/Vendor-Finanzierung

Die auffälligste Strukturbeobachtung ist die **Kreislauffinanzierung**. Am 23.09.2025 sagte Nvidia bis zu 100 Mrd. USD Investment in OpenAI zu, gekoppelt an den Aufbau von mindestens 10 GW Nvidia-Systemen; OpenAI-CFO Sarah Friar räumte ein, „most of the money will go back to Nvidia" (Fortune, 28.09.2025; The Register, 04.11.2025). Im Oktober 2025 folgte ein AMD-Deal: OpenAI verpflichtet sich zu 6 GW AMD-Instinct-GPUs, AMD gewährt im Gegenzug einen Warrant auf bis zu 160 Mio. Aktien (rund 10 % Stake) (Vested Finance, Oktober 2025). Nvidia investierte am 26.01.2026 zusätzlich 2 Mrd. USD in das hochverschuldete CoreWeave (TechCrunch, 26.01.2026). Insgesamt summieren sich OpenAIs Infrastruktur-Verpflichtungen 2025 auf rund 1 Bio. USD, nach anderer Zählung bis 1,4 Bio. USD über acht Jahre.

Diese Strukturen sind starke **Blasen-Strukturindizien** – sie können Nachfrage künstlich stützen und externalisieren Risiko über SPVs (Oracle, Meta, xAI, CoreWeave verlagerten laut Berichten rund 120 Mrd. USD KI-Infrastrukturschulden off-balance-sheet). Für die *spezifische* Hypothese „Firmen erwarten Crash" sind sie jedoch **ambivalent bis neutral**: Wer solche Deals eingeht, ist dadurch massiv long positioniert, nicht abgesichert. Es sind Wetten auf Fortsetzung, nicht auf einen Crash.

Die extreme Diskrepanz zwischen Umsatz und Verlust unterstreicht das Blasenrisiko, widerspricht aber der Crash-Erwartung im Verhalten: OpenAIs Umsatz 2025 lag bei rund 13,1 Mrd. USD (+118 %) bei einem operativen Verlust von rund 20,9 Mrd. USD; der Cash-Burn wird auf rund 27 Mrd. (2026) bis rund 63 Mrd. (2027) projiziert, Cashflow-Positivität erst um 2029/2030 (Fortune, 12.11.2025; **Schätzungen Sacra – nicht testierte Rechnungslegung**). Trotzdem folgte im März 2026 eine 122-Mrd.-USD-Runde bei 852 Mrd. USD Bewertung. **Sämtliche dieser Umsatz-, Verlust- und Burn-Zahlen stammen aus Schätzungen (Sacra) und geleakten Dokumenten – nicht aus geprüfter Rechnungslegung; Größenordnungen konsistent, Details unbestätigt.**

Zwei Signale verdienen gesonderte Erwähnung. OpenAI-CFO Friar brachte Anfang November 2025 einen staatlichen „backstop" für Compute-Finanzierung ins Spiel und ruderte nach Empörung zurück („muddied the point"); Altman betonte, das Unternehmen wolle keine Staatsgarantien (CNBC, 06.11.2025). Diese zurückgezogene Äußerung über *Chip-Finanzierungsgarantien* als Crash-nahes Signal zu lesen wäre eine Überdehnung; sie ist bestenfalls ein **sehr schwaches, ambivalentes** Indiz dafür, dass die Verpflichtungen als kapitalseitig herausfordernd wahrgenommen werden – und wird unten entsprechend *nicht* in die „Für"-Spalte einsortiert. Demgegenüber warnt Dario Amodei, bei nur einem Jahr Fehleinschätzung der Wachstumskurve drohe Bankrott, agiert aber bewusst kapital-diszipliniert und bleibt bullish auf die Technologie (Fortune, 14.02.2026). (Die früher kolportierte Angabe, Anthropic habe „rund 4× geringere Compute-Kosten als OpenAI", lässt sich nicht primärquellenbasiert belegen und wird hier als unbestätigte Kolportage nicht weitergeführt.) Amodei anerkennt also Downside, ohne die eigene Firma auf einen Crash zu positionieren.

**Zwischenfazit B:** Die zirkulären Strukturen sind das stärkste *objektive* Blasenindiz, aber neutral für die Verhaltenshypothese. Das Finanzierungsverhalten der Kernlabore entspricht einem „Gewinner-take-most"-Wetten auf Fortsetzung, nicht einer eingepreisten Korrektur.

---

## 4. Indikator C – Der Capex-Boom als Gegenargument

Der Infrastruktur-Befund spricht per Saldo **eher gegen** die Hypothese. Die dominante *revealed preference* ist der Kapitaleinsatz: Die vier großen Hyperscaler planen für 2026 zusammen rund 725 Mrd. USD, ein Plus von 77 % gegenüber rund 410 Mrd. USD (2025) – Amazon rund 200, Google rund 185, Meta rund 125, Microsoft rund 120 Mrd. (Statista/Tom's Hardware/CNBC, Q1 2026). Rund 75 % entfallen direkt auf KI-Infrastruktur. Stargate wurde als „ahead of schedule" beschrieben, mit rund 7 GW geplanter Kapazität und über 400 Mrd. USD Investition über drei Jahre (OpenAI/SoftBank PR, September 2025). Wer intern einen nahen Crash erwartet, baut keine mehrjährigen, kapitalintensiven, teils schuldenfinanzierten Assets.

Es gibt jedoch echte, datierte **Vorsichtssignale**, die die Hypothese punktuell tangieren. Microsoft stornierte Anfang 2025 mehrere hundert MW an Rechenzentrums-Leases; TD Cowen deutete eine mögliche „oversupply position" an (Fortune, 24.02.2025). Satya Nadella räumte öffentlich einen „overbuild" ein und kündigte an, 2027/28 stärker zu leasen als selbst zu bauen (Dwarkesh-Patel-Interview, 2025). Amazon verkürzte die Nutzungsdauer bestimmter Server von sechs auf fünf Jahre (rückwirkend zum 01.01.2025), was schnellere Obsoleszenz der GPU-Assets bilanziell eingesteht (Amazon 10-K/Earnings, 07.02.2025).

Diese Signale zeigen **Kalibrierung und Risikomanagement einzelner Akteure, keinen koordinierten Rückzug** – und sind darum *ambivalent*, nicht eindeutig pro Hypothese. Nadella bleibt voll investiert; Amazon erhöhte den Capex trotzdem; und Meta *verlängerte* 2025 gegenläufig die Nutzungsdauern – eine uneinheitliche Bilanzierung, die eine klare *revealed-preference*-Deutung erschwert. Wichtig auch: Die „oversupply"-Einschätzung stammt von einem Analysten (TD Cowen), nicht aus Firmen-Guidance.

**Zwischenfazit C:** Fortgesetztes, sogar beschleunigtes Bauen mit punktueller Vorsicht. Eine Crash-Erwartung „der Firmen selbst" wird durch den Capex-Boom nicht belegt; die Vorsichtssignale sind Risikomanagement, kein defensives Positionieren.

---

## 5. Indikator D – Führungsaussagen und Insider-Signale

### Stated Preferences: der stärkste Pro-Teil – mit einer wichtigen Einschränkung

Auf Aussagenebene stützen die Befunde die Hypothese ungewöhnlich stark. Sam Altman sagte im August 2025 wörtlich: „Are we in a phase where investors as a whole are overexcited about AI? My opinion is yes." Milliardenbewertungen für Startups mit „three people and an idea" seien „insane"; „Someone is going to lose a phenomenal amount of money. We don't know who." (CNBC, 18.08.2025). OpenAI-Chairman Bret Taylor bestätigte am 15.09.2025 den Dotcom-Vergleich: „A lot of people will lose a lot of money." (Fortune, 15.09.2025).

**Interpretatorischer Vorbehalt:** Diese Zitate zeigen präzise auf *andere* – überbewertete Startups, „investors as a whole", unbekannte Verlierer. Sie sind ebenso konsistent mit einem **„Flucht-in-Qualität-innerhalb-der-Blase"**-Narrativ, in dem der Sprecher die eigene Firma als Überlebenden positioniert, wie mit einer Selbst-Crash-Erwartung. Als Beleg dafür, dass das jeweilige Kernlabor *für sich selbst* einen Einbruch einpreist, taugen sie deshalb nur eingeschränkt.

Mark Zuckerberg nannte einen „collapse" der KI-Blase „definitely a possibility" und akzeptierte das Risiko, „a couple hundred billion dollars" fehlzuinvestieren – wertete aber das Verpassen der KI-Chance als das größere Risiko (Fortune, 19.09.2025; **Wortlaut über „definitely a possibility" hinaus nur mittelbar/paywall-belegt**). Demis Hassabis sprach von „obviously a bubble in the private market" (zitiert u. a. Forbes, 31.05.2025; MIT Technology Review, 15.12.2025). Sundar Pichai räumte „some irrationality" ein und warnte, „no company is going to be immune, including us." (Axios, 18.11.2025). Pichais Formulierung ist – anders als Altmans – ausdrücklich selbstinkludierend und damit das für die Hypothese trennschärfste Aussagensignal.

### Der wichtigste Gegenbeleg auf Aussagenebene

Jensen Huang widerspricht offensiv: „There's been a lot of talk about an AI bubble. From our vantage point, we see something very different"; er rahmt die Lage als „the largest infrastructure build-out in human history" (Fortune, 21.01.2026).

### Revealed Preferences der Insider

Laut SEC Form 4 verkauften Insider von Nvidia, Palantir und Broadcom in den zwölf Monaten bis 28.04.2026 rund 4,6 Mrd. USD bei nahezu null Käufen – Nvidia rund 2,4 Mrd., Palantir über 1 Mrd., Broadcom rund 1,14 Mrd.; das Sell/Buy-Verhältnis der Nvidia-Insider lag bei 15:0 (The Motley Fool, 06.01.2026 & 04.05.2026). CEO Jensen Huang verkauft im Rahmen seines vorab festgelegten 10b5-1-Plans; die dokumentierten Planvolumina liegen grob bei rund 700 Mio. USD (2024) und bis rund 865 Mio. USD (2025), kumuliert also in der Größenordnung von rund 1–1,7 Mrd. USD über das Fenster – **nicht** in dem früher kolportierten Umfang von 2,9 Mrd. USD, der zudem mit den 2,4 Mrd. USD *aller* Nvidia-Insider im selben Zeitraum unvereinbar wäre. Diese Zahl wird hier entsprechend korrigiert.

**Drei entscheidende Einschränkungen** entwerten dieses Signal weit stärker als der 10b5-1-Vorbehalt allein: (1) Die Verkäufe laufen über vorab festgelegte Pläne (Diversifikation). (2) Es handelt sich um börsennotierte **Chip- und Analytics-Firmen** – nicht um die strategischen Kernlabore, deren interne Crash-Erwartung die eigentliche Hypothese ist; die Zurechnung ist damit periphär. (3) **Base-Rate:** Nahezu null Insiderkäufe und hohe Sell/Buy-Verhältnisse (15:0) sind bei Mega-Cap-Tech der historische Normalzustand, weil Vergütung überwiegend aktienbasiert erfolgt und Insider strukturell Netto-Verkäufer sind – unabhängig von jeder Blasen-Sicht. Das „Kein-Insider-kauft-nach"-Argument verliert vor dieser Base-Rate fast seine gesamte Aussagekraft.

Ein Einzelfall bleibt spekulativ: Palantir-CEO Alex Karp nannte den Short-Seller Michael Burry im November 2025 öffentlich „batshit crazy" und reichte laut Berichten kurz darauf ein Filing zum Verkauf von rund 96 Mio. USD Aktien ein – Karp verkauft jedoch routinemäßig über 10b5-1-Pläne; Kausalität unbestätigt (Fortune, 04.11.2025; **Konfidenz niedrig**).

**Zwischenfazit D:** Die Akteure erkennen und benennen die Blase offen (stützt – am trennschärfsten bei Pichai), verhalten sich operativ aber wie Überzeugte, die weiter investieren (widerspricht der engen Lesart). Das scheinbar stärkste Pro-Verhaltenssignal (Insiderverkäufe) ist durch 10b5-1-Automatik, Peripherie-Zuordnung und Base-Rate dreifach konfundiert und liefert netto kaum Evidenz.

---

## 6. Indikator E – Skeptiker, ROI-Zweifel und externe Warnungen

Ein breiter externer Skepsis-Diskurs untermauert das objektive Blasenrisiko, ist aber für die Verhaltenshypothese primär **neutral**, weil er nicht von den KI-Firmen ausgeht. Die MIT-NANDA-Studie „The GenAI Divide" fand, dass trotz 30–40 Mrd. USD Enterprise-Investment 95 % der GenAI-Pilotprojekte keinen messbaren P&L-Effekt liefern (Fortune, 18.08.2025; **Methodik-Kritik existiert**). IWF und Bank of England warnten im Oktober 2025 vor einer „sharp/abrupt correction" und zogen Dotcom-Parallelen – relativierten aber, der Boom sei nicht kreditgetrieben, sondern von cash-reichen Konzernen finanziert (CNBC, 09.10.2025). Die BIS warnte im Juni 2026 vor über 1 Bio. USD Hyperscaler-Capex 2025–2026 und zog Parallelen zu historischen Investitionsblasen mit Rezessions-Endpunkt (Fortune, 29.06.2026).

Michael Burry (Scion) baute Put-Positionen auf Nvidia und Palantir mit Nominalwert rund 1,38 Mrd. USD auf (tatsächliche Prämie deutlich geringer) und nannte Nvidia „a Cisco at the center of it all" (Fortune, 04.11.2025). Sein Vorwurf, Hyperscaler blähten Gewinne durch zu lange Chip-Abschreibungsdauern auf, zielt direkt auf das Verhalten der Firmen (CNBC, 11.11.2025; **Primärseite lieferte HTTP 403, nur über Suchindex bestätigt – Vorwurf entsprechend vorsichtig attribuiert**). Apollo-Chefökonom Torsten Slok hält die Top-10 des S&P 500 heute für stärker überbewertet als in den 1990ern und warnt vor „painful repricing" (Fortune, 06.07.2026). JPMorgan-CEO Jamie Dimon sieht KI als „real", erwartet aber Verschwendung eines Teils der Investitionen (**Sekundärbezug**).

**Zwischenfazit E:** Diese Befunde belegen Blasen-Sorgen Dritter, nicht die Erwartung der Unternehmen. Sie verstärken die Kontextfrage, nicht die Kernhypothese.

---

## 7. Der Bull-Case (Steelman): Warum das Verhalten rational statt defensiv ist

Die stärkste Gegenposition argumentiert, dass das Verhalten der KI-Firmen eine rationale Reaktion auf reale, kapazitätsbegrenzte Nachfrage ist. Der Kern ist *revealed-preference*-Logik: Wer einen Crash erwartet, geht keine mehrjährigen, nicht stornierbaren Compute-Verpflichtungen ein, keine Capex-Steigerungen um 77 % und keine langlaufenden Abnahmeverträge – er zieht Kapital ab.

Die Nachfragefundamente sind real und beschleunigen. Nvidias Data-Center-Umsatz erreichte in Q1 FY2027 (endete 26.04.2026) 75,2 Mrd. USD (+92 % YoY), der Gesamtumsatz 81,6 Mrd. (+85 %); Blackwell sei „off the charts", Cloud-GPUs ausverkauft (Nvidia SEC 8-K, Mai 2026). Anthropics Run-Rate stieg von rund 9 Mrd. USD (Ende 2025) auf geschätzt rund 47 Mrd. (Mai 2026), mit über 1.000 Enterprise-Kunden über 1 Mio. USD/Jahr (VentureBeat/Sacra, Mai 2026; **Schätzung**). OpenAIs Run-Rate erreichte Mitte 2026 rund 25 Mrd. USD (Sacra/mlq.ai; **Schätzung**).

Der Engpass ist das Angebot, nicht die Nachfrage: Microsofts Backlog verdoppelte sich auf rund 625 Mrd. USD (Fortune/Futurum, 28.01.2026; **gegen MSFT-Earnings zu verifizieren**); Nadella berichtete von GPUs, die mangels Strom nicht angeschlossen werden können („a bunch of chips sitting in inventory that I can't plug in"). Die tatsächliche Nutzung wächst laut Sekundärberichten um Größenordnungen: Google soll im Mai 2026 rund 3,2 Billiarden Token/Monat verarbeitet haben, 7× YoY (Cryptobriefing/Tomasz Tunguz, 2026; **Sekundärquelle, gegen Google-Earnings zu verifizieren**). Und die Enterprise-Adoption ist noch frühphasig – laut McKinsey nutzen 88 % der Organisationen KI in mindestens einer Funktion, aber nur rund 7 % haben unternehmensweit skaliert (McKinsey, State of AI 2025; **Skalierungsquote gegen Primärstudie zu verifizieren**) – großer Wachstumsvorlauf statt Sättigung. Auch die IPOs lassen sich als nachfragegetrieben lesen: Cerebras war im Mai 2026 über 20-fach überzeichnet (Morningstar/NAI500, 2026).

**Ehrlichkeitseinschränkung des Bull-Case:** Diese Befunde widerlegen primär „Firmen erwarten Crash", nicht die separate Frage, ob objektiv eine Blase besteht. Starkes Umsatzwachstum und rationale Investitionslogik können mit einer Bewertungsblase koexistieren (Eisenbahn-/Fiber-Analogie: echte Nachfrage plus Überinvestition). Und die selbstinkludierenden Bubble-Eingeständnisse (Pichai) bleiben als Spannung stehen. Zudem stützen sich mehrere der stärksten Bull-Zahlen (Run-Rates, Token-Volumen, Skalierungsquote) auf Sekundär- oder Schätzquellen.

---

## 8. Kontextfrage (getrennt gehalten): Ist es objektiv eine Blase?

Diese Frage ist **kein Beleg** für die Kernhypothese, wird aber zur Einordnung beantwortet. Die objektive Blasenfrage weist *mehr* Indizien auf als die Verhaltenshypothese. Dafür sprechen strukturelle Marker: eine CAPE-Ratio über 40 (ein Niveau, das zuvor nur 1999/2000 und ab 2021 erreicht wurde); die extreme Umsatz-Verlust-Diskrepanz bei OpenAI (rund 13–25 Mrd. Umsatz gegen rund 21 Mrd. operativen Verlust und bis 1,4 Bio. Ausgabenzusagen); die von Sequoias David Cahn geprägte „600-Milliarden-Frage" zur Capex-Umsatz-Lücke – ursprünglich sein Juni-2024-Framework (Fortschreibung seiner 200-Mrd.-Frage von 2023), 2026 medial fortgeschrieben (Forbes, 02.06.2026); die MIT-Studie (95 % der Pilotprojekte ohne P&L-Effekt); und vor allem die zirkuläre Vendor-Finanzierung mit rund 120 Mrd. USD Off-Balance-SPV-Schulden. Offizielle Institutionen (IWF, Bank of England, BIS) warnen explizit.

Gegen eine *reine* Blase sprechen real und stark beschleunigende, zahlungswirksame Umsätze (Nvidia +92 % DC, Token-Volumen laut Sekundärbericht 7×, breite Enterprise-Adoption mit erst rund 7 % Skalierung) sowie eine cash-reiche statt kreditgetriebene Hauptfinanzierung. Das plausibelste Kontexturteil ist eine **koexistente Realität**: echte Nachfrage *und* Kapital-Fehlallokation/Überbewertung – wahrscheinlich eine partielle Bewertungsblase bei realem Technologiekern.

**Entscheidend:** Selbst wenn objektiv eine Blase vorliegt, belegt das nicht, dass die Firmen selbst mit ihrem Platzen rechnen.

---

## 9. Synthese und Gesamturteil

Die zentrale Spannung ist die systematische **Divergenz zwischen Kommunikation und Kapitalallokation**. Dieselben CEOs, die 2025 öffentlich „Blase", „Kollaps möglich" und „jemand verliert ein Vermögen" sagen, erhöhen zeitgleich massiv ihre langfristigen, teils nicht stornierbaren, teils schuldenfinanzierten Investitionen (Meta über 600 Mrd., OpenAI rund 1,4 Bio. Zusagen, Hyperscaler +77 % Capex). Da bei Konflikt *revealed > stated* gewichtet wird, entkräftet das Handeln die wörtlichen Warnungen als Beleg für eine interne Crash-Erwartung. Zudem zielen mehrere Aussagen (Altman, Taylor) explizit auf *andere* Marktteilnehmer – ein Flucht-in-Qualität-Framing, das die eigene Firma als Überlebenden positioniert. Die Aussagen erscheinen daher eher als **Risiko-Framing, Reputations-Hedging oder „talking the book"** denn als Vorbote defensiver Positionierung.

Verschärft wird die Spannung dadurch, dass das scheinbar stärkste Handlungssignal – Insiderverkäufe – dreifach konfundiert ist (10b5-1-Automatik, Peripherie-Zuordnung, Base-Rate der Optionsvergütung), dass die Gründer-Cash-outs durch Lock-up-Mechanik und hohe Halte-Quoten (CoreWeave-Gründer halten rund 18 %) entwertet werden, und dass direkt daneben ein **gegenläufiges** Handlungssignal steht: Anthropic-Insider halten ihre Anteile. Die Auflösung ist heterogen: Cash-out konzentriert sich bei bereits liquiden oder peripheren Akteuren (CoreWeave-Gründer, Magnetar, Chip-Insider), Doubling-down bei den strategischen Kernlaboren.

**Abwägung:**

| | Für die Hypothese | Gegen die Hypothese | Ambivalent / Risikomanagement |
|---|---|---|---|
| **Stated** | Pichai (selbstinkludierend); Altman, Zuckerberg, Hassabis, Amodei benennen Blase/Irrationalität | Huang bestreitet die Blase offensiv; Warnende bleiben voll investiert; Altman/Taylor zeigen auf *andere* | – |
| **Revealed** | Breites Cash-out (CoreWeave, Magnetar, OpenAI-Mitarbeiter) – *nach Confounder-Abzug schwach* | Capex +77 % auf ~725 Mrd.; teils nicht stornierbare Verpflichtungen bis 2031; Anthropic-Insider halten; hohe Gründer-Halte-Quoten; kein belegtes Put-Hedging der Firmen | Amazon 6→5 Jahre Abschreibung; Microsoft-Lease-Stornierungen; Friar-„backstop"; Chip-Insider-Verkäufe (Base-Rate/Peripherie) |
| **Kontext** | CAPE > 40; zirkuläre Finanzierung; MIT 95 %; IWF/BoE/BIS-Warnungen; IPO-Timing im Warnfenster | Nvidia +92 % DC; Backlog ~625 Mrd.; Token 7×; cash-finanziert | – |

**Gesamturteil:** Die Firmen **erkennen und benennen** das Blasenrisiko offen, verhalten sich operativ aber wie auf Fortsetzung Wettende („Rennen bis zuletzt", Winner-take-most), nicht wie für einen Crash Positionierte. Punktuelle Vorsicht (Amazon-Abschreibung, Microsoft-Lease-Stornierungen, Nadellas „overbuild") zeigt Risikomanagement, keinen koordinierten Rückzug. Die **starke Hypothese ist überwiegend nicht gestützt**; die **schwache Hypothese** – Realisieren von Buchgewinnen bei Höchstbewertung – ist **teilweise gestützt**, aber nach Bereinigung um Confounder (10b5-1, Lock-up-Mechanik, Diversifikation, Base-Rate, Mitarbeiterliquidität, zwingender Kapitalbedarf, Makro-/CFIUS-Faktoren) bleibt das Netto-Signal **schwach**. Konfidenz: mittel.

---

## 10. Limitationen, offene Fragen und Datenlücken

- **Keine internen Dokumente:** Ob Firmen intern einen Crash modellieren, ist nicht belegbar; alle Signale sind extern beobachtet – Inferenz, kein direkter Erwartungsbeleg.
- **Direktestes Hedging-Signal fehlt:** Keine Belege für Kursabsicherungen (Collars/Puts), Netto-Short-Positionen von Insidern auf eigene Aktien, Insider-getriebenen Put-Skew oder Krisen-Cash-Hortung. Wäre dieses Signal vorhanden, wäre es der sauberste Beleg – es fehlt oder existiert nicht öffentlich.
- **Base-Rate und 10b5-1-Anteil unvollständig ausgewiesen:** Insiderverkäufe bei Mega-Cap-Tech sind strukturell (Optionsvergütung) und über vorab terminierte Pläne getrieben; die exakte Aufschlüsselung „Diversifikation/Base-Rate vs. Crash-Erwartung" ist aus Sekundärquellen nur teilweise dokumentiert. Konkret sind die Huang-Verkaufsvolumina hier auf Basis dokumentierter Planvolumina (~1–1,7 Mrd. USD) korrigiert; eine vollständige SEC-Form-4-Verifikation über das gesamte Fenster steht aus.
- **Private Finanzzahlen unbestätigt:** Umsatz-, Verlust- und Run-Rate-Zahlen der Kernlabore (OpenAI, Anthropic, xAI) stammen überwiegend aus Schätzungen (Sacra/mlq.ai) oder Leaks – keine testierte Rechnungslegung; Größenordnungen konsistent, Details unbestätigt.
- **Bull-Case-Kennzahlen teils sekundär:** Token-Volumen (7×), Microsoft-Backlog (~625 Mrd.) und die McKinsey-Skalierungsquote (~7 %) sind load-bearing, stammen aber aus Sekundär- bzw. noch nicht gegen die Primärstudien/Earnings verifizierten Quellen.
- **Vertragsdesign ungeprüft:** Take-or-pay-Klauseln, Kündigungsrechte, Liquidationspräferenzen und SPV-Risikotragung sind nicht primärquellenbasiert geprüft – entscheidend für die Frage, wer bei einem Einbruch das Downside trägt.
- **Korrelation ≠ Kausalität:** „IPO-/Tender-Rush = Crash-Antizipation" ist nicht trennscharf von konkurrierenden Erklärungen (zwingender Kapitalbedarf, normalisiertes IPO-Fenster, Mitarbeiterliquidität, Lock-up-Mechanik, VC-Fondszyklen). Die CAPE-IPO-Koinzidenz ist Kontext, kein Verhaltensbeleg.
- **Uneinheitliche Branchensignale:** Amazon verkürzt Abschreibungsdauern, Meta verlängert sie; „oversupply" stammt von Analysten, nicht aus Firmen-Guidance; die tatsächliche Auslastung der neuen 2026er-Kapazität ist unbelegt.
- **Einzelne Quellen eingeschränkt:** CNBC-Artikel zu Burrys Abschreibungsvorwurf (11.11.2025) lieferte HTTP 403; Zuckerbergs Volltext ist paywall-bedingt nur mittelbar belegt; The-Information-14-Mrd.-Zahl ist ein Paywall-Sekundärzitat; die Karp-Burry-Chronologie ist auf November 2025 zu datieren.

---

## 11. Quellenverzeichnis

1. Bloomberg, „CoreWeave Founders Have Sold $2.3 Billion in Stock Since IPO", 09.06.2026.
2. Bloomberg/Crain's Chicago Business, „CoreWeave founders aren't the only ones selling: Magnetar halves its stake", 09.06.2026.
3. Seeking Alpha, „CoreWeave founders sold $2.3B in planned stock sales since IPO (halten ~18 %)", 09.06.2026.
4. CNBC, „OpenAI wraps $6.6 billion share sale at $500 billion valuation", 02.10.2025.
5. The Information, „OpenAI, Anthropic Employees Have Already Cashed Out About $14 Billion", Anfang 2026 (*unbestätigt – Paywall/Sekundärzitat*).
6. TechCrunch/Financial Times, „Elon Musk's xAI reportedly looks to raise $300M in tender offer", 02.06.2025.
7. Fortune, „2026 is looking like 1999… bubble fears… IPO", 08.06.2026.
8. CNBC, „CoreWeave prices IPO at $40 a share, below expected range", 27.03.2025.
9. Bloomberg, „Anthropic Completes Tender Offer, But Employees Hold Onto Shares", 08.04.2026.
10. Bloomberg, „Data Center IPOs Set to Raise Billions", 06.05.2026.
11. Tech Startups, „AI chipmaker Cerebras revives IPO plans after $1.1B raise and CFIUS clearance", 19.12.2025.
12. Fortune, „Nvidia-OpenAI circular financing / AI bubble", 28.09.2025.
13. The Register, „The circular economy of AI", 04.11.2025.
14. Vested Finance, „How OpenAI, Nvidia, AMD and Oracle minted $1 trillion", Oktober 2025.
15. Fortune, „OpenAI cash burn rate / annual losses", 12.11.2025; Sacra, sacra.com/c/openai (*Schätzung*).
16. TechCrunch, „Nvidia invests $2B to help debt-ridden CoreWeave", 26.01.2026.
17. CNBC, „OpenAI's Sam Altman warns AI market is in a bubble", 18.08.2025.
18. Fortune, „OpenAI board chair Bret Taylor — AI bubble Dotcom comparison", 15.09.2025.
19. CNBC, „OpenAI CFO Sarah Friar says company is not seeking government backstop", 06.11.2025.
20. TechCrunch, „Anthropic raises $6.5 billion, nears $1T valuation ahead of IPO", 28.05.2026; Anthropic, Series H.
21. Fortune, „Anthropic CEO Dario Amodei — spending, capex risk, bankruptcy", 14.02.2026.
22. TechCrunch, „Anthropic CEO weighs in on AI bubble talk", 04.12.2025.
23. CNBC, „Elon Musk xAI raises $20 billion from Nvidia, Cisco investors", 06.01.2026; Sacra, sacra.com/c/xai (*Schätzung*).
24. Statista (chart/35046), Tom's Hardware, CNBC, Hyperscaler-Capex 2026, 06.02.2026.
25. OpenAI, „Five new Stargate sites"; SoftBank Group PR, 24.09.2025.
26. TD Cowen via Fortune, Microsoft-Lease-Stornierungen, 24.02.2025.
27. Dwarkesh-Patel-Interview / Yahoo Finance / Tom's Hardware, Nadella „overbuild", 2025.
28. Amazon 10-K/Earnings via Deep Quarry/Calcbench, Abschreibungsverkürzung, 07.02.2025.
29. CNBC, Michael Burry — Abschreibungsvorwurf, 11.11.2025 (*HTTP 403, nur Suchindex; Vorwurf vorsichtig attribuiert*).
30. Forbes, Sequoia/David Cahn — „$600B question" (ursprünglich Juni 2024, fortgeschrieben), 02.06.2026.
31. Yahoo Finance/MarketBeat, CoreWeave-Insiderverkäufe, 12.07.2026; TechTimes, 12.07.2026.
32. Fortune, „Zuckerberg says an AI bubble collapse is definitely a possibility", 19.09.2025 (*Volltext mittelbar/paywall*).
33. Forbes, „Jensen Huang and Dario Amodei on AI", 31.05.2025; MIT Technology Review, 15.12.2025.
34. Axios, „Google CEO AI bubble warning — no company immune, including us", 18.11.2025.
35. Fortune, „Jensen Huang — largest infrastructure build-out in history", 21.01.2026; NPR, 23.11.2025.
36. The Motley Fool, „NVDA, PLTR, AVGO send Wall Street $4.6 billion warning", 06.01.2026 & 04.05.2026.
37. Fortune, „Big Short investor Michael Burry — Nvidia and Palantir puts / Alex Karp", 04.11.2025 (Karp-Burry-Episode: November 2025).
38. Fortune, „MIT report: 95% of generative AI pilots at companies are failing", 18.08.2025 (MIT NANDA; *Methodik-Kritik*).
39. CNBC, „IMF and Bank of England join chorus warning of an AI bubble", 09.10.2025.
40. Fortune, „BIS annual report — $1 trillion AI investment boom", 29.06.2026.
41. Fortune, „AI productivity gains bubble painful repricing — Torsten Slok", 06.07.2026; Futurism.
42. NPR, „Concerns about an AI bubble are bigger than ever", 23.11.2025; JPMorgan/Dimon-Interviews 2025 (*Sekundärbezug*).
43. Nvidia SEC 8-K, Q1 FY2027 (Data Center 75,2 Mrd., +92 %), Mai 2026.
44. VentureBeat/Simon Willison/PYMNTS/Sacra, Anthropic-Run-Rate ~47 Mrd. und Enterprise-Kunden, April–Mai 2026 (*Schätzung*).
45. mlq.ai/Sacra, OpenAI Run-Rate ~25 Mrd., 2026 (*Schätzung*).
46. McKinsey, „The State of AI: Global Survey 2025" (*Skalierungsquote gegen Primärstudie zu verifizieren*).
47. WSJ via Datacenterdynamics/Data Center Frontier/OpenAI, OpenAI-Oracle-Vertrag, September 2025 / Update April 2026.
48. Fortune/Futurum, Microsoft-Backlog ~625 Mrd., 28.01.2026 & Q3 FY2026 (*gegen MSFT-Earnings zu verifizieren*).
49. Cryptobriefing/Tomasz Tunguz, Google Token-Volumen 7× YoY, Mai 2026 (*Sekundärquelle*).
50. Morningstar/Motley Fool/NAI500, Cerebras IPO überzeichnet, Mai 2026; CoreWeave, März 2026.
51. Fortune, „CoreWeave IPO — not a good proxy for AI boom-bust", 28.03.2025; CNBC, 27.03.2025 & 30.03.2025.

*Hinweis zu Zitaten: Wörtlich wiedergegebene Aussagen (Altman, Huang, Zuckerberg „definitely a possibility", Pichai, Hassabis, Friar) stammen aus den oben genannten, datierten Beiträgen. Finanzkennzahlen privater Firmen (OpenAI, Anthropic, xAI) sowie Token-Volumen, Microsoft-Backlog und die McKinsey-Skalierungsquote beruhen überwiegend auf Schätzungen oder Sekundärquellen und sind als unbestätigt gekennzeichnet. Die Huang-Verkaufssumme ist gegenüber einer früheren Fassung auf dokumentierte 10b5-1-Planvolumina (~1–1,7 Mrd. USD) korrigiert. Wo Primärquellen nicht direkt abrufbar waren (Burry-CNBC 403, Zuckerberg-Paywall, The-Information-14-Mrd.), ist dies vermerkt. Die CAPE-Marke über 40 wurde historisch 1999/2000 und ab 2021 erreicht.*