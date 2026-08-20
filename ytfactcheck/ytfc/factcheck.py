"""Faktencheck mit Claude — bewusst in zwei getrennten Schritten.

Schritt 1 extrahiert *ueberpruefbare Behauptungen* aus dem Transkript.
Schritt 2 prueft jede einzeln **mit Websuche**.

Die Trennung ist kein Stilmittel. Ein Sprachmodell, das aus dem Gedaechtnis
"faktencheckt", erfindet selbstbewusst Zahlen und kennt nichts nach seinem
Trainingsstand. Ein Urteil entsteht hier nur aus Quellen, die im selben
Durchlauf tatsaechlich gefunden wurden — und "nicht ueberpruefbar" ist ein
vollwertiges, ausdruecklich erwuenschtes Ergebnis.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field

import anthropic

WEB_SEARCH_TOOL = {"type": "web_search_20260209", "name": "web_search"}
MAX_PAUSE_RESUMES = 5

VERDICTS = (
    "belegt",
    "groesstenteils_richtig",
    "kontextfehlend",
    "irrefuehrend",
    "falsch",
    "nicht_ueberpruefbar",
)
PROBLEM_VERDICTS = ("falsch", "irrefuehrend", "kontextfehlend")

# --- Schemata --------------------------------------------------------------

CLAIMS_SCHEMA = {
    "type": "object",
    "properties": {
        "topic": {"type": "string"},
        "claims": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "claim": {"type": "string"},
                    "quote": {"type": "string"},
                    "timestamp": {"type": "string"},
                    "category": {
                        "type": "string",
                        "enum": ["zahl_statistik", "ereignis", "zitat",
                                 "wissenschaft", "recht_gesetz", "sonstiges"],
                    },
                    "checkworthiness": {"type": "integer", "minimum": 1, "maximum": 5},
                    "why": {"type": "string"},
                },
                "required": ["claim", "quote", "timestamp", "category",
                             "checkworthiness", "why"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["topic", "claims"],
    "additionalProperties": False,
}

VERDICT_SCHEMA = {
    "type": "object",
    "properties": {
        "verdict": {"type": "string", "enum": list(VERDICTS)},
        "confidence": {"type": "string", "enum": ["niedrig", "mittel", "hoch"]},
        "one_liner": {"type": "string"},
        "explanation": {"type": "string"},
        "what_is_true": {"type": "string"},
        "sources": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "url": {"type": "string"},
                    "publisher": {"type": "string"},
                    "stance": {
                        "type": "string",
                        "enum": ["stuetzt", "widerspricht", "teilweise", "kontext"],
                    },
                },
                "required": ["title", "url", "publisher", "stance"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["verdict", "confidence", "one_liner", "explanation",
                 "what_is_true", "sources"],
    "additionalProperties": False,
}

# --- Prompts ---------------------------------------------------------------

EXTRACT_SYSTEM = """\
Du extrahierst aus einem YouTube-Transkript diejenigen Aussagen, die sich \
gegen die Wirklichkeit pruefen lassen.

Eine Behauptung gehoert in die Liste, wenn sie
- eine konkrete Tatsache benennt (Zahl, Datum, Ereignis, Studie, Gesetz, Zitat),
- prinzipiell durch eine Quelle bestaetigt oder widerlegt werden kann,
- und zentral fuer die Aussage des Videos ist.

Nicht in die Liste gehoeren: Meinungen, Wertungen, Prognosen, Witze, \
Hypothesen, rhetorische Fragen, Geschmacksurteile und alles was mit "ich \
finde", "vermutlich" oder "koennte sein" markiert ist. Im Zweifel weglassen \
statt aufnehmen.

Formuliere jede Behauptung so um, dass sie ohne den Rest des Videos \
verstaendlich ist (Pronomen aufloesen). "quote" ist der WOERTLICHE \
Transkriptausschnitt, unveraendert. "timestamp" ist der Zeitstempel der Zeile, \
in der die Aussage faellt, im Format des Transkripts.

checkworthiness 1-5: Wie viel Schaden richtet die Aussage an, wenn sie falsch \
ist und stehen bleibt? 5 = eine zentrale, schaedliche, breit geteilte \
Falschaussage. 1 = eine Randnotiz.

Sortiere absteigend nach checkworthiness."""

RESEARCH_SYSTEM = """\
Du recherchierst EINE Behauptung aus einem YouTube-Video mit der Websuche.

Vorgehen:
1. Suche gezielt nach der urspruenglichen Quelle (Primaerquelle: Statistikamt, \
   Studie, Gesetzestext, Gerichtsurteil, Originalzitat) — nicht nach \
   Berichten ueber Berichte.
2. Suche zusaetzlich nach Belegen, die der Behauptung WIDERSPRECHEN. Wenn du \
   nur bestaetigende Quellen suchst, findest du auch nur bestaetigende.
3. Pruefe, ob eine korrekte Zahl irrefuehrend verwendet wird: falscher \
   Bezugszeitraum, fehlende Bezugsgroesse, Korrelation als Kausalitaet, \
   Zitat aus dem Zusammenhang gerissen. Das ist der haeufigste Fall — \
   haeufiger als eine glatt erfundene Zahl.
4. Achte auf das Datum. Eine Zahl, die 2019 stimmte, stimmt heute vielleicht \
   nicht mehr.

Halte am Ende ausdruecklich fest:
- was du gefunden hast, mit Quelle und Datum,
- was du NICHT herausfinden konntest,
- ob die gefundenen Quellen wirklich voneinander unabhaengig sind (drei \
  Zeitungen, die dieselbe Agenturmeldung abschreiben, sind EINE Quelle).

Erfinde nichts. Wenn die Suche nichts Belastbares hergibt, sag das deutlich."""

JUDGE_SYSTEM = """\
Du bringst ein abgeschlossenes Rechercheprotokoll in eine feste Form. Du \
recherchierst nicht nach und ergaenzt kein Wissen aus dem Gedaechtnis — du \
darfst dich ausschliesslich auf das Protokoll stuetzen.

Urteile:
- belegt: Mehrere unabhaengige Quellen bestaetigen die Aussage.
- groesstenteils_richtig: Im Kern richtig, Details ungenau.
- kontextfehlend: Fuer sich genommen richtig, aber es fehlt etwas \
  Entscheidendes, das den Eindruck kippt.
- irrefuehrend: Die Zahlen stimmen, die daraus gezogene Schlussfolgerung \
  nicht.
- falsch: Quellen widersprechen der Aussage klar.
- nicht_ueberpruefbar: Die Recherche hat nichts Belastbares ergeben.

nicht_ueberpruefbar ist KEIN Scheitern, sondern das ehrliche Ergebnis, wann \
immer die Quellenlage duenn, widerspruechlich oder nur mittelbar ist. \
"Ich habe keinen Beleg gefunden" heisst nicht "die Aussage ist falsch" — \
verwechsle das nie. Fuer "falsch" brauchst du eine Quelle, die aktiv \
widerspricht, nicht das Ausbleiben einer bestaetigenden.

confidence bezieht sich auf die Qualitaet der Quellenlage, nicht darauf, wie \
sicher du dich fuehlst.

"one_liner": ein Satz, allgemeinverstaendlich, ohne Fachjargon.
"what_is_true": bei falsch/irrefuehrend/kontextfehlend die Richtigstellung in \
ein bis zwei Saetzen; sonst leer lassen.
"sources": nur URLs, die im Protokoll wirklich vorkommen."""

RHETORIC_SYSTEM = """\
Du analysierst, WIE ein Video argumentiert — nicht ob die Einzelfakten \
stimmen (das wird separat geprueft).

Benenne, jeweils mit woertlichem Beleg aus dem Transkript, nur was du \
tatsaechlich vorfindest:
- Auslassungen: Was muesste man wissen, das nicht vorkommt?
- Framing: Wortwahl, die eine Wertung transportiert.
- Quellenumgang: Werden Quellen genannt? Nachpruefbar? Richtig wiedergegeben?
- Verallgemeinerungen vom Einzelfall aufs Ganze.
- Emotionale Verstaerker anstelle von Belegen.

Sei fair und praezise. Beschreibe die Technik, unterstelle keine Absicht und \
diagnostiziere keine Motive. Wenn das Video sauber argumentiert, sag das — \
eine erwartete Auffaelligkeit nicht zu finden ist ein Ergebnis, kein \
Versaeumnis. Erfinde nichts, um die Liste zu fuellen."""


# --- Datenklassen ----------------------------------------------------------


@dataclass
class Claim:
    claim: str
    quote: str
    timestamp: str
    category: str
    checkworthiness: int
    why: str


@dataclass
class Checked:
    claim: Claim
    verdict: str
    confidence: str
    one_liner: str
    explanation: str
    what_is_true: str
    sources: list[dict]
    research_notes: str = ""

    @property
    def is_problem(self) -> bool:
        return self.verdict in PROBLEM_VERDICTS


@dataclass
class Report:
    video_id: str
    title: str
    channel: str
    risk: str
    topic: str
    transcript_source: str
    checked: list[Checked] = field(default_factory=list)
    rhetoric: str = ""
    usage: dict = field(default_factory=dict)

    @property
    def problems(self) -> list[Checked]:
        return [c for c in self.checked if c.is_problem]


# --- Claude-Aufrufe --------------------------------------------------------


class FactChecker:
    def __init__(self, model: str, client: anthropic.Anthropic | None = None):
        self.model = model
        self.client = client or anthropic.Anthropic()
        self.usage = {"input": 0, "output": 0, "calls": 0}

    def _track(self, msg) -> None:
        self.usage["calls"] += 1
        self.usage["input"] += getattr(msg.usage, "input_tokens", 0) or 0
        self.usage["output"] += getattr(msg.usage, "output_tokens", 0) or 0

    @staticmethod
    def _text(msg) -> str:
        return "\n".join(b.text for b in msg.content if b.type == "text").strip()

    @staticmethod
    def _json(msg) -> dict:
        # output_config.format garantiert gueltiges JSON im Textblock
        return json.loads(next(b.text for b in msg.content if b.type == "text"))

    # -- Schritt 1: Behauptungen finden ------------------------------------

    def extract_claims(self, transcript_text: str, title: str,
                       max_claims: int) -> tuple[str, list[Claim]]:
        user = (
            f"Videotitel: {title}\n\n"
            f"Transkript (mit Zeitstempeln):\n\n{transcript_text}\n\n"
            f"Extrahiere hoechstens {max_claims} ueberpruefbare Behauptungen."
        )
        # Transkripte sind lang -> streamen, damit kein HTTP-Timeout zuschlaegt.
        with self.client.messages.stream(
            model=self.model,
            max_tokens=16000,
            thinking={"type": "adaptive"},
            output_config={
                "effort": "medium",
                "format": {"type": "json_schema", "schema": CLAIMS_SCHEMA},
            },
            system=[{
                "type": "text",
                "text": EXTRACT_SYSTEM,
                "cache_control": {"type": "ephemeral"},  # stabil ueber alle Videos
            }],
            messages=[{"role": "user", "content": user}],
        ) as stream:
            msg = stream.get_final_message()
        self._track(msg)
        data = self._json(msg)
        claims = [Claim(**c) for c in data["claims"]][:max_claims]
        return data.get("topic", ""), claims

    # -- Schritt 2a: recherchieren (mit Websuche) --------------------------

    def _research(self, claim: Claim, title: str, channel: str,
                  effort: str, min_sources: int) -> str:
        user = (
            f"Video: {title!r} vom Kanal {channel!r}\n"
            f"Zeitstempel: {claim.timestamp}\n"
            f"Woertlich gesagt: {claim.quote!r}\n\n"
            f"Zu pruefende Behauptung: {claim.claim}\n\n"
            f"Recherchiere sie. Ziel sind mindestens {min_sources} voneinander "
            f"unabhaengige Quellen. Erreichst du das nicht, halte das fest — "
            f"eine duenne Quellenlage ist ein Ergebnis."
        )
        messages = [{"role": "user", "content": user}]
        resumes = 0
        while True:
            msg = self.client.messages.create(
                model=self.model,
                max_tokens=16000,
                thinking={"type": "adaptive"},
                output_config={"effort": effort},
                system=[{
                    "type": "text",
                    "text": RESEARCH_SYSTEM,
                    "cache_control": {"type": "ephemeral"},
                }],
                tools=[{**WEB_SEARCH_TOOL, "max_uses": 4 + min_sources}],
                messages=messages,
            )
            self._track(msg)
            if msg.stop_reason != "pause_turn" or resumes >= MAX_PAUSE_RESUMES:
                break
            # Serverseitige Tool-Schleife pausiert -> Antwort anhaengen und
            # erneut senden; der Server macht dann selbst weiter.
            messages.append({"role": "assistant", "content": msg.content})
            resumes += 1
        return self._text(msg)

    # -- Schritt 2b: Urteil in feste Form bringen --------------------------

    def _judge(self, claim: Claim, notes: str, min_sources: int) -> dict:
        user = (
            f"Geprueft wurde: {claim.claim}\n"
            f"Woertlich im Video: {claim.quote!r}\n\n"
            f"Rechercheprotokoll:\n\n{notes}\n\n"
            f"Fasse das Ergebnis zusammen. Liegen weniger als {min_sources} "
            f"unabhaengige Quellen vor, ist 'nicht_ueberpruefbar' oder "
            f"confidence 'niedrig' angemessen."
        )
        msg = self.client.messages.create(
            model=self.model,
            max_tokens=4000,
            thinking={"type": "adaptive"},
            output_config={
                "effort": "low",  # reine Formatierung, keine neue Denkleistung
                "format": {"type": "json_schema", "schema": VERDICT_SCHEMA},
            },
            system=[{
                "type": "text",
                "text": JUDGE_SYSTEM,
                "cache_control": {"type": "ephemeral"},
            }],
            messages=[{"role": "user", "content": user}],
        )
        self._track(msg)
        return self._json(msg)

    def check_claim(self, claim: Claim, title: str, channel: str,
                    effort: str, min_sources: int) -> Checked:
        notes = self._research(claim, title, channel, effort, min_sources)
        v = self._judge(claim, notes, min_sources)
        return Checked(
            claim=claim,
            verdict=v["verdict"],
            confidence=v["confidence"],
            one_liner=v["one_liner"],
            explanation=v["explanation"],
            what_is_true=v["what_is_true"],
            sources=v["sources"],
            research_notes=notes,
        )

    # -- Schritt 3: Einordnung (nur problematische Kanaele) ----------------

    def analyse_rhetoric(self, transcript_text: str, title: str) -> str:
        msg = self.client.messages.create(
            model=self.model,
            max_tokens=8000,
            thinking={"type": "adaptive"},
            output_config={"effort": "high"},
            system=[{
                "type": "text",
                "text": RHETORIC_SYSTEM,
                "cache_control": {"type": "ephemeral"},
            }],
            messages=[{
                "role": "user",
                "content": f"Videotitel: {title}\n\nTranskript:\n\n{transcript_text}",
            }],
        )
        self._track(msg)
        return self._text(msg)
