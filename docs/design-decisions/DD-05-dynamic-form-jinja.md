---
title: DD-05
parent: Design Decisions
---

{: .no_toc }
# 05: Dynamische Formularzeilen – Jinja2-Schleife vs. Client-JavaScript

## Meta

Status
: **Decided**

Updated
: 23-Jun-2026

## Problem Statement

Ein Creator muss für einen Hive unbegrenzt viele Rabatt-Staffeln hinzufügen können (z. B. Staffel 1: Ab 10 Stück, Staffel 2: Ab 20 Stück usw.). Da laut Dozenten Vorgabe absolut kein JavaScript auf Client Seite erlaubt ist, können wir nicht einfach per JS neue Eingabefelder im Browser generieren. 

Wie schaffen wir es trotzdem, dass das Formular dynamisch wächst, ohne die bisherigen Benutzereingaben zu löschen?

## Decision

Wir lösen das Problem über einen sauberen Server roundtrip in Flask und eine Jinja2 Schleife im HTML. 

Wenn der User auf „+ Weitere Staffel hinzufügen“ klickt, wird das Formular per POST abgeschickt. Das Backend fängt den Wert `action == "add_tier"` ab, speichert die aktuellen Eingaben in einer Liste, hängt ein leeres Feld hinten an und rendert das Template über eine Jinja-Schleife (`range(thresholds|length)`) sofort neu.

*Decision was taken by:* Darian Omorowa

## Regarded options

We regarded two alternative options:

+ JS-DOM-Manipulation: Neue Felder per JavaScript im Browser erzeugen
+ Flask-POST und Jinja2: Formular an den Server schicken und mit einer Zeile mehr neu laden lassen

| Kriterium | JavaScript | Flask-POST + Jinja2 |
| --- | --- | --- |
| **Vorgaben-Erfüllung** | ❌ Verbotener Einsatz von clientseitigem JS | ✔️ Erfüllt die Dozenten Regeln zu 100% |
| **Performance** | ✔️ Fühlt sich flüssiger an, ohne Neuladen | ❌ Seite lädt beim Hinzufügen einer Zeile kurz neu |
| **Stabilität im Browser** | ❌ JS-Bugs könnten das Formular im Browser einfrieren lassen oder kaputte Zeilen erzeugen | ✔️ Fehlerfrei, da der Server bei jedem Klick eine komplett saubere, frische HTML Seite zurückschickt |