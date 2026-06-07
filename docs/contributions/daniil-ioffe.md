---
title: Daniil Ioffe
parent: Individual Contributions
nav_order: 1
---

{: .no_toc }
# Daniil Ioffe

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Meta-Goals

### Target grade

Meine Zielnote für dieses Modul ist **1,0**.

### Personal goals

Meine persönlichen Ziele in diesem Modul sind, Python besser zu lernen, sicherer im Präsentieren zu werden und Teamarbeit in einem Softwareprojekt professioneller zu gestalten.

Außerdem möchte ich lernen, wie man eine technische Umsetzung nicht nur als Code betrachtet, sondern auch mit Produktidee, Zielgruppe und strategischem Denken verbindet.

Dat Spannende an DealHive ist, dass wir nicht einfach irgendeine Web-App bauen, sondern eine Idee mit konkretem Domainbezug entwickeln.

---

## Eidesstattliche Erklärung (Stand 17.05.2026)

**[Daniil Ioffe, Matrikelnr.: 77203498549]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Käufer-Bereich mit Hive-Übersicht, Detailseite und Spielsystem-Filter angefangen | Dadurch gibt es jetzt einen ersten funktionierenden Teil der App. Hives werden aus SQLite gelesen, in `/hives` angezeigt und können über `/hives/<id>` im Detail geöffnet werden. Der Filter nach Spielsystem passt außerdem gut zum Domainbezug. | Ich musste Flask-Routes, SQLite-Abfragen und Templates miteinander verbinden und dabei verstehen, wie die Daten von der Datenbank bis zur HTML-Seite kommen. |
| 2 | Überarbeitung des Projektkonzepts mit klarem Domainbezug auf Brettspiele, TTRPGs, Tabletops und Zubehör | Dadurch wurde DealHive konkreter und weniger generisch. Die App wirkt jetzt eher wie ein echtes Produkt für eine bestimmte Community. | Die ursprüngliche Idee war noch sehr allgemein. Nach Rücksprache mit Herrn Eck mussten wir sie so zuschneiden, dass sie weiterhin einfach umsetzbar bleibt, aber fachlich klarer wird. |
| 3 | Dokumentation und UI-Skizzen in Richtung DealHive-Domain überarbeitet | Ich habe geholfen, unsere bisherigen Inhalte in die FSWD-Template-Struktur zu bringen und die Screens stärker auf Sammelkäufe im Hobbybereich auszurichten. | Die Herausforderung war, nicht einfach das Template zu füllen, sondern unsere bestehende Idee, Product Discovery, Screens und Contributions nachvollziehbar zusammenzubringen. |

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Käufer-Bereich für DealHive angefangen | Branch `feature/hives-overview-detail`, Dateien `app.py`, `database.py`, `test_database.py`, `templates/hives.html`, `templates/hive_detail.html` | FSWD-Kursmaterial, eigene Umsetzung, Teamabstimmung |
| Hive-Übersicht `/hives` gebaut | Route in `app.py`, Template `templates/hives.html` | Eigene Umsetzung, SQLite-Testdaten |
| Detailseite für einzelne Hives gebaut | Route `/hives/<id>` in `app.py`, Template `templates/hive_detail.html` | Eigene Umsetzung, SQLite-Testdaten |
| Hives in SQLite gespeichert und ausgelesen | Datei `database.py`, Tabelle `hives` mit Titel, Spielsystem, Kurzbeschreibung, Beschreibung, Deadline und Teilnehmerzahlen | Teamabstimmung zum Datenmodell, Feedback von Herrn Eck |
| Testdaten für Hives erstellt und getestet | Datei `test_database.py`, lokaler Test mit `python test_database.py` | Eigene Tests, KI-unterstützte Testdatenliste |
| Einfachen Filter nach Spielsystem eingebaut | Filterlogik in `app.py`, Dropdown in `templates/hives.html` | Feedback von Herrn Eck, Teamentscheidung nur wenige sinnvolle Filter zu nutzen |
| HTML aus `app.py` in eigene Templates verschoben | Dateien `templates/hives.html` und `templates/hive_detail.html` | Flask-Template-Ansatz aus dem Kurs |
| Domainbezug für DealHive ausgearbeitet | Dokumentation in [Value Proposition](../01-value-proposition.md), [Design Challenge](../product-discovery/01-design-challenge.md) und [Solution Elements](../product-discovery/03-solution-elements.md) | Eigene Projektidee, Teamdiskussion, bestehender Value Proposition Canvas |
| Bestehende Projektidee auf Brettspiele, TTRPGs und Tabletop-Zubehör angepasst | [Target Users + Problems](../product-discovery/02-users-problems.md), [Solution Elements](../product-discovery/03-solution-elements.md) | Ursprünglicher Value Proposition Canvas, eigene Überarbeitung |
| UI-Screens mit stärkerem Domainbezug überarbeitet | Wireframes im Ordner `../product-discovery/material/03-se/ui-screens/` | Bestehende UI-Skizzen, eigene Überarbeitung, ChatGPT Image Generation |
| Dokumentation in das FSWD-Template übertragen | Dateien im `/docs`-Ordner, besonders Product Discovery und Contributions | FSWD-App-Template des Kurses |
| Eigene Contribution-Seite gepflegt | Diese Datei | FSWD Contribution Template |

## AI Directory

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  | ChatGPT | Unterstützung beim Sortieren und Strukturieren eigener Notizen und Projektideen | Teile der Dokumentation im `/docs`-Ordner | Die Inhalte wurden von mir geprüft, angepasst und nicht unverändert übernommen. |
| 02  | ChatGPT | Sprachliche Überarbeitung einzelner deutscher Dokumentationstexte | Product Discovery, Value Proposition, Contributions | Nutzung als Formulierungshilfe. Die fachlichen Inhalte stammen aus der Gruppenidee und wurden manuell angepasst. |
| 03 | ChatGPT Image Generation | Einfache UI-Skizzen-Anpassung auf Basis unserer vorhandenen Skizzen | UI-Screens im Bereich Product Discovery | Die Prompts und Anpassungswünsche wurden manuell gesteuert. Die Ergebnisse wurden geprüft und ausgewählt. Keine autonome Bearbeitung des Projekts. |
| 04  | ChatGPT | Unterstützung bei Git- und Template-Fragen | Arbeit am Branch `docs-template` und `feature/hives-overview-detail` | Nutzung als Schritt-für-Schritt-Hilfe. Befehle wurden manuell ausgeführt und kontrolliert. |
| 05 | ChatGPT | Unterstützung bei Coding-Fragen und Fehlersuche | `app.py`, `database.py`, `test_database.py`, `templates/hives.html`, `templates/hive_detail.html` | Nutzung als Hilfe beim Verständnis von Flask-Routen, SQLite-Abfragen, Templates und Fehlermeldungen. Code wurde manuell eingefügt, lokal getestet und angepasst. |
| 06 | ChatGPT | Unterstützung bei einfachen Testdaten für Hives | `test_database.py` | Die Liste mit Beispiel-Hives wurde mit KI-Unterstützung erstellt. Die Daten wurden manuell eingefügt, geprüft und an unser Datenmodell angepasst. |
| 07 | ChatGPT | Unterstützung beim Überarbeiten der eigenen Contribution-Seite | `docs/contributions/daniil-ioffe.md` | Nutzung als Formulierungshilfe für meine eigenen Beiträge und den AI-Directory-Abschnitt. Inhalte wurden manuell geprüft und angepasst. |