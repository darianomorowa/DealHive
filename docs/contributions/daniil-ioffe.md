---

title: Daniil Ioffe
parent: Individual Contributions
nav_order: 1
------------

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

Das Spannende an DealHive ist, dass wir nicht einfach irgendeine Web-App bauen, sondern eine Idee mit konkretem Domainbezug entwickeln. Gerade durch den Fokus auf Brettspiele, TTRPGs, Tabletop und Zubehör wurde aus einer allgemeinen Plattformidee ein konkreteres Produkt.

---

## Eidesstattliche Erklärung (Stand 23.06.2026)

**[Daniil Ioffe, Matrikelnr.: 77203498549]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten, einschließlich KI-generierter Inhalte, ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| #  | My contribution                                                     | Why I am proud of it                                                                                                                                                                                                                                                                               | Which challenge I overcame                                                                                                                                                                                                                                                                             |
| :- | :------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | Integration, Strukturierung und Stabilisierung der Flask-App        | Ich habe stark daran mitgearbeitet, dass DealHive nicht nur aus einzelnen Seiten besteht, sondern als zusammenhängende Flask-App funktioniert. Dazu gehören Routing, Layout, Sidebar, Session-Navigation, Hive-Flows und die Integration verschiedener Teambeiträge.                               | Die größte Herausforderung war, dass viele Features parallel auf unterschiedlichen Branches entstanden sind. Dadurch mussten Merges vorbereitet, Konflikte verstanden und Änderungen so zusammengeführt werden, dass die App danach noch startet und fachlich Sinn ergibt.                             |
| 2  | Creator-nahe Hive-Funktionen und Zugriffskontrolle weiterentwickelt | Mein Schwerpunkt lag nicht auf dem gesamten Hive-System allein, sondern vor allem auf Creator-Funktionen, Integration, Bearbeitung, Zugriffskontrolle und Preisbearbeitung. Wichtig war dabei, dass Creator nicht einfach fremde Hives bearbeiten können, sondern nur die eigenen Hives verwalten. | Ich musste verstehen, wie `hives`, `users`, `user_hives`, `hive_tiers`, Sessions und Creator-Routen zusammenspielen. Gerade bei Hive-Bearbeitung, Rabattstaffeln und Ownership-Checks war es wichtig, nicht nur UI-Buttons einzubauen, sondern den Datenfluss und die Berechtigungen sauber zu halten. |
| 3  | Dokumentation, Design Decisions und Gesamtbild des Projekts         | Ich habe viel daran gearbeitet, die technische Umsetzung in verständliche Dokumentation zu übersetzen. Dazu gehören Design Decisions, Contribution-Struktur, Domain-Fokus, UI-Entscheidungen und Erklärungen für die mündliche Prüfung.                                                            | Die Herausforderung war, aus vielen einzelnen Commits und Branches ein nachvollziehbares Gesamtbild zu machen. Man musste erkennen, welche Entscheidung wirklich wichtig ist, welche Features zusammengehören und wie man das so erklärt, dass es nicht wie nachträglich zusammengeworfen wirkt.       |

## Contributions

| Contribution                                                                              | Proof, e.g., git commits                                                                                                                                                                             | Sources used                                                                                 |
| :---------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| Käufer-Bereich mit Hive-Übersicht, Detailseite und Spielsystem-Filter angefangen          | Branch `feature/hives-overview-detail`, Dateien `app.py`, `database.py`, `test_database.py`, `templates/hives.html`, `templates/hive_detail.html`                                                    | [HWR FSWD-Kursmaterial](https://hwrberlin.github.io/fswd/), eigene Umsetzung, Teamabstimmung |
| Hive-Übersicht `/hives` aufgebaut und mit SQLite-Daten verbunden                          | Route `/hives`, Template `templates/hives.html`, Funktion `get_all_hives()`                                                                                                                          | HWR FSWD-Kursmaterial, Flask/Jinja-Grundlagen aus dem Kurs, eigene Tests                     |
| Detailseite für einzelne Hives umgesetzt                                                  | Route `/hives/<int:hive_id>`, Template `templates/hive_detail.html`, Funktion `get_hive_by_id(hive_id)`                                                                                              | HWR FSWD-Kursmaterial, eigene Umsetzung                                                      |
| Spielsystem-Filter bereinigt und stärker an die DealHive-Domain angepasst                 | Commit `Hive Filter Kategorien bereinigt`, Datei `templates/hives.html`                                                                                                                              | Teamfeedback, Feedback von Herrn Eck, eigene Überarbeitung                                   |
| Gemeinsames Layout und Sidebar weiterentwickelt                                           | Dateien `templates/layout.html`, `templates/partials/sidebar.html`                                                                                                                                   | HWR FSWD-Kursmaterial, Jinja-Template-Ansatz, eigene Umsetzung                               |
| Session-Navigation und Rollenwechsel in der Sidebar verbessert                            | Commit `Verbessere Hive Formular Layout und Session Navigation`, Datei `templates/partials/sidebar.html`, Route `/session/role`                                                                      | HWR FSWD-Kursmaterial, Flask-Session-Logik, eigene Tests                                     |
| Inline-JavaScript aus dem Rollenwechsel entfernt und durch einen normalen Button ersetzt  | Commit `kleine, sehr unbedeutende Fehlerchen behoben`, Datei `templates/partials/sidebar.html`                                                                                                       | Kursvorgabe ohne eigenes JavaScript, eigene Anpassung                                        |
| Creator Dashboard auf eingeloggten Creator umgestellt beziehungsweise integriert          | Commit `Creator Dashboard Zuordnung und Contact Button nicht mehr doppelt drin`, Dateien `creator_routes.py`, `database.py`                                                                          | Teamarchitektur, SQLite mit `execute`, eigene Umsetzung und Integration                      |
| Neu erstellte Hives direkt dem aktuellen Creator zugeordnet                               | Funktion `assign_hive_to_user(...)`, Datei `creator_routes.py`                                                                                                                                       | Bestehendes Datenmodell, Teamabstimmung                                                      |
| Doppelten Creator-Kontakt-Button entfernt                                                 | Commit `Creator Dashboard Zuordnung und Contact Button nicht mehr doppelt drin`, Datei `templates/hive_detail.html`                                                                                  | Eigene UI-Kontrolle, Testen im Browser                                                       |
| Hive-Formular optisch verbessert und stärker an das gemeinsame Layout angepasst           | Commit `Verbessere Hive Formular Layout und Session Navigation`, Datei `templates/create_hive.html`                                                                                                  | Bestehendes `layout.html`, eigene UI-Anpassung                                               |
| Hive-Bearbeitung für Creator ergänzt und integriert                                       | Commit `Hive-Bearbeitung(mit Datenbank),gitignore, kleine UI fixes`, Dateien `creator_routes.py`, `database.py`, `templates/edit_hive.html`                                                          | HWR FSWD-Kursmaterial, SQLite, Flask-Routing, eigene Umsetzung                               |
| Update-Funktion für bestehende Hives ergänzt                                              | Funktion `update_hive(...)` in `database.py`                                                                                                                                                         | SQLite mit `connection.execute(...)`, eigene Umsetzung                                       |
| Creator-Ownership-Check bei Hive-Bearbeitung eingebaut                                    | Route `/creator/hives/<int:hive_id>/edit`, Funktionen `get_hive_by_id(...)`, `get_hive_creator_id(...)`                                                                                              | Teamentscheidung zu Rollen und Zugriff, eigene Umsetzung                                     |
| Rabattbearbeitungslogik und Preisbearbeitungslogik erweitert                              | Commit `Rabattbearbeitungslogik+Prüfmechanismus hinzugefuegt und Pricing-Bugs gefixt`, Dateien `creator_routes.py`, `database.py`, `pricing_logic.py`, `templates/edit_hive.html`                    | Eigene Umsetzung, Teamabstimmung, SQLite, Python-Grundlagen                                  |
| Bearbeitung bestehender Rabattstaffeln im Edit-Formular ermöglicht                        | Funktionen `get_hive_tiers(...)`, `replace_hive_tiers(...)`, Template `edit_hive.html`                                                                                                               | Bestehende Rabattlogik, eigene Erweiterung                                                   |
| Schutz bereits erreichter Rabattstaffeln konzeptionell und technisch vorbereitet          | Datei `pricing_logic.py`, Funktion `active_discount_was_lowered(...)`, Anzeige gesperrter Staffeln in `edit_hive.html`                                                                               | Eigene fachliche Überlegung, Teamfeedback                                                    |
| `.gitignore` erweitert, damit lokale Analyse-Dateien nicht versehentlich committed werden | Commit `Hive-Bearbeitung(mit Datenbank),gitignore, kleine UI fixes`, Datei `.gitignore`                                                                                                              | Eigene Projektorganisation                                                                   |
| Mehrere Pull Requests und Branches gemergt oder beim Zusammenführen unterstützt           | Merge Commits, unter anderem `Feature/hive chat`, `Feature/hive pricing tiers`, `Use buttons in creator dashboard`, `Document database model`                                                        | Git/GitHub, Teamarbeit, eigene Konfliktanalyse                                               |
| Merge-Konflikte und kaputte Stellen nach Branch-Zusammenführungen analysiert              | Git-Historie, lokale Tests, Fehlersuche in `app.py`, `hives.py`, `creator_routes.py`, `sidebar.html`                                                                                                 | Git/GitHub, eigene Tests, ChatGPT als Erklärhilfe                                            |
| Gesamtstruktur der App nach Merges geprüft                                                | Lokales Starten der Flask-App, Prüfung von Navigation, Sessions, Hives, Creator Dashboard und Templates                                                                                              | Eigene Tests, Teamabstimmung                                                                 |
| Domainbezug für DealHive geschärft                                                        | Dokumentation in [Value Proposition](../01-value-proposition.md), [Design Challenge](../product-discovery/01-design-challenge.md), [Solution Elements](../product-discovery/03-solution-elements.md) | Teamdiskussion, Feedback von Herrn Eck, eigene Überarbeitung                                 |
| UI-Skizzen und Screen-Beschreibungen auf die DealHive-Domain angepasst                    | Wireframes im Bereich `product-discovery/material/03-se/ui-screens/`                                                                                                                                 | Eigene Überarbeitung, Teamfeedback, KI-gestützte Bild- und Textarbeit                        |
| Design Decisions für zentrale technische Entscheidungen vorbereitet und formuliert        | Dateien im Bereich `docs/design-decisions/`                                                                                                                                                          | Eigene Analyse des Codes, Teamabstimmung, HWR FSWD-Template                                  |
| Eigene Contribution-Seite überarbeitet und an den aktuellen Projektstand angepasst        | Diese Datei `docs/contributions/daniil-ioffe.md`                                                                                                                                                     | HWR FSWD-Template, eigene Reflexion                                                          |
| Projektstruktur und Dokumentation regelmäßig auf Konsistenz geprüft                       | Dateien im `/docs`-Ordner, Contributions, Design Decisions, README- und Pages-Struktur                                                                                                               | HWR FSWD-Template, eigene Kontrolle                                                          |

## Abgrenzung zu Teambeiträgen

Einige Teile von DealHive hängen technisch eng zusammen. Deshalb ist mir wichtig, meinen Beitrag nicht so darzustellen, als hätte ich alles alleine gebaut.

| Bereich  | Schwerpunkt                                                                                                                                                                   |
| :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Haya     | Buyer-Flow, insbesondere „Meine Hives“, Join-Bestätigung, Käufernavigation und Anpassungen an bestehenden Dateien                                                             |
| Darian   | Dynamic Pricing, Rabattstaffeln, Chat-MVP, Käuferübersicht für Creator und weitere Hive-Erweiterungen                                                                         |
| Matthieu | Profilbereich, Profilbearbeitung, Data-Model-Dokumentation und Teile des Creator Dashboards                                                                                   |
| Daniil   | Integration, Refactoring, Sidebar/Layout, Creator-Zuordnung, Hive-Bearbeitung, Pricing-Bearbeitung, Merge-Analyse, Dokumentationsstruktur und Product-Owner-nahe Koordination |

Zusätzlich habe ich im Projekt teilweise eine Product-Owner-nahe Rolle übernommen. Damit meine ich nicht, dass ich allein entschieden habe, was gebaut wird, sondern dass ich oft versucht habe, das Gesamtbild zusammenzuhalten: Was ist DealHive eigentlich, welche Features passen wirklich zur Idee, was ist zu groß für unseren aktuellen Stand und wie erklären wir das Projekt sinnvoll in der Dokumentation. Außerdem habe ich Aufgabenpakete verteilt und darauf geachtet, dass die Arbeit im Team sinnvoll aufgeteilt ist. Das lag mir auch deshalb nahe, weil mich die Produktidee und der Domainbezug persönlich interessiert haben.

## Eigene Netto-Code-Zeilen im Teamvergleich

Die folgende Tabelle basiert auf der aktuellen Commit-Auswertung nach dem Merge der Buyer-Flow- und Buyer-Overview-Branches. Gezählt wurden nur nicht gemergte, App-bezogene Erstcommits nach Author. Reine Merge-Commits, Dokumentationsdateien, Contribution-Seiten, Design Decisions und Assets sind hier nicht enthalten. Gezählt wurden vor allem Python-Dateien, Jinja-/HTML-Templates und kleinere Projektorganisationsdateien wie `.gitignore`.

| Person   | App-bezogene Erstcommits | Additions | Deletions | Bearbeitete Zeilen | Netto-Zeilen |
| :------- | -----------------------: | --------: | --------: | -----------------: | -----------: |
| Daniil   |                       23 |     1.864 |       629 |              2.493 |       +1.235 |
| Matthieu |                       11 |       981 |       137 |              1.118 |         +844 |
| Darian   |                       34 |       801 |       224 |              1.025 |         +577 |
| Haya     |                       13 |       699 |       236 |                935 |         +463 |

Die Zahlen sind keine perfekte Leistungsbewertung. Sie zeigen nur, wie viele App-bezogene Zeilen nach dieser Zählweise zuerst von wem committed wurden. Merge-Commits zählen hier bewusst nicht als neue Codeleistung, weil sie sonst fremde Branch-Inhalte demjenigen zurechnen würden, der den Merge durchgeführt hat.

Besonders bei Haya zeigt die reine Netto-Zahl den Beitrag nur eingeschränkt. Ihr Buyer-Flow hat viele bestehende Dateien verändert, zum Beispiel Routen, Templates, Sidebar, Join-Bestätigung und Buyer-Übersicht. Dadurch entstehen viele Additions, aber auch viele Deletions. Netto bleibt dann weniger übrig, obwohl fachlich ein kompletter Buyer-Flow integriert wurde. Deshalb ist die Spalte „Bearbeitete Zeilen“ wichtig: Sie zeigt besser, wie viel bestehender App-Code tatsächlich angefasst wurde.

Mein Beitrag lag besonders darin, Funktionen zusammenzuführen, technische Zusammenhänge zu verstehen, Creator-nahe Abläufe weiterzuentwickeln, eine Product-Owner-nahe Perspektive einzubringen und das Projekt in Code und Dokumentation konsistenter zu machen.


## Design Decisions

| Design Decision                                         | My relation to it                                                                                                             | Why it matters                                                                                                           |
| :------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| DD-04: User-Hive-Beziehungen über `user_hives` abbilden | Diese Entscheidung ist wichtig für Creator-Zuordnung, Buyer-Beitritte und Mengenlogik.                                        | Ohne `user_hives` wäre schwer erklärbar, welcher User welchen Hive erstellt hat oder welchem Hive beigetreten ist.       |
| DD-06: Flask-Routen nach Verantwortlichkeit aufteilen   | Ich habe stark an Integration und Refactoring gearbeitet und kann erklären, warum `app.py` sonst zu unübersichtlich wurde.    | Die Entscheidung verbessert Teamarbeit, Merging und Wartbarkeit.                                                         |
| DD-07: Gemeinsames Jinja-Layout und Sidebar nutzen      | Ich habe an Layout, Sidebar und Navigation mitgearbeitet.                                                                     | Die Entscheidung sorgt dafür, dass Seiten einheitlich wirken und Navigation nicht in jeder Datei neu gebaut werden muss. |
| DD-09: Headless API für Hives bereitstellen             | Ich kann erklären, wie sich die API von der SQLite-Datei unterscheidet und warum sie für die Projektanforderung relevant ist. | Sie zeigt, dass DealHive nicht nur HTML-Seiten rendert, sondern ausgewählte Daten auch als JSON bereitstellen kann.      |

## AI Directory

| #  | AI Tool                  | Purpose of Use                                                                   | Affected Sections (Code + Docs)                                                       | Remarks, Procedure, Prompts                                                                                                                                                                                                                                                                                    |
| -- | ------------------------ | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 01 | ChatGPT                  | Code erklären und Verständnis von Flask, SQLite, Jinja und Sessions verbessern   | `app.py`, `hives.py`, `creator_routes.py`, `user_routes.py`, `database.py`, Templates | Nutzung als Erklärhilfe. Der Code wurde von mir gelesen, angepasst, manuell eingefügt und lokal getestet. Beispielprompt: „Erklär mir bitte Schritt für Schritt, wie diese Flask-Route mit der SQLite-Funktion zusammenarbeitet.“                                                                              |
| 02 | ChatGPT                  | Unterstützung bei Fehlersuche und Featureoptimierung                             | Hive-Übersicht, Detailseite, Sidebar, Hive-Bearbeitung, Rabattstaffeln, Pricing-Logik | Nutzung zur Analyse von Fehlermeldungen, kaputten Flows und möglichen Verbesserungen. Beispielprompt: „Warum funktioniert diese Route nach dem Merge nicht mehr und welche Datei sollte ich zuerst prüfen?“                                                                                                    |
| 03 | ChatGPT                  | Unterstützung bei Git-, Branch- und Merge-Fragen                                 | Branches, Pull Requests, Merge-Konflikte, lokale Git-Befehle                          | Nutzung als Schritt-für-Schritt-Hilfe bei Git und Merges. Befehle wurden manuell ausgeführt und kontrolliert. Beispielprompt: „Ich bin auf Branch X, möchte Änderungen aus Branch Y übernehmen und vorher nichts kaputt machen. Welche Git-Befehle brauche ich?“                                               |
| 04 | ChatGPT                  | Unterstützung beim Gesamtbild des Projekts und bei der Analyse von Team-Branches | Contributions, Design Decisions, Branch-Analyse, mündliche Prüfungsvorbereitung       | Nutzung, um besser zu verstehen, welche Features Teammitglieder gebaut haben und wie sie technisch zusammenhängen. Beispielprompt: „Analysiere diese Commit-Historie und fasse zusammen, wer vermutlich welche Projektteile umgesetzt hat.“                                                                    |
| 05 | ChatGPT                  | Sprachliche Überarbeitung und bessere Lesbarkeit von Dokumentationstexten        | Product Discovery, Value Proposition, Contributions, Design Decisions                 | Nutzung als Formulierungshilfe. Inhalte wurden von mir geprüft und angepasst. Beispielprompt: „Formuliere diesen Abschnitt verständlicher und passend für eine technische Projektdokumentation.“                                                                                                               |
| 06 | ChatGPT Image Generation | Unterstützung bei einfachen UI-Skizzen und visuellen Varianten                   | UI-Screens im Bereich Product Discovery                                               | Die Prompts und Anpassungswünsche wurden manuell gesteuert. Ergebnisse wurden geprüft, ausgewählt und inhaltlich an DealHive angepasst. Beispielprompt: „Erstelle eine einfache Wireframe-Skizze für eine Web-App-Seite mit Hive-Übersicht, Filter und Kartenlayout.“                                          |
| 07 | ChatGPT                  | Unterstützung beim Strukturieren der Design Decisions                            | `docs/design-decisions/`                                                              | Nutzung zur Strukturierung und sprachlichen Ausarbeitung. Die fachlichen Entscheidungen stammen aus unserem Projektverlauf und wurden mit dem Code abgeglichen. Beispielprompt: „Schreibe eine Design Decision zu SQLite mit execute statt db.query, menschlich formuliert und mit betrachteten Optionen.“     |
| 08 | ChatGPT                  | Unterstützung beim Überarbeiten dieser eigenen Contribution-Seite                | `docs/contributions/daniil-ioffe.md`                                                  | Nutzung als Formulierungshilfe für meine eigenen Beiträge und den AI-Directory-Abschnitt. Inhalte wurden von mir geprüft und an meine tatsächliche Arbeit angepasst. Beispielprompt: „Hier ist unsere Gesamtcommitübersicht, bitte nach meinen Commits Filtern und eine übersicht meiner Leistungen erstellen“ |
