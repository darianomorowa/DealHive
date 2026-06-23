---

title: Matthieu Weinlein
parent: Individual Contributions
nav_order: 4
---

{: .no_toc }

# Matthieu Weinlein

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

Ich möchte in diesem Kurs meine Fähigkeiten in der Webentwicklung mit Python weiter verbessern und besser verstehen, wie man eine vollständige Webanwendung strukturiert, plant und technisch umsetzt.

Außerdem ist es mein Ziel, sauberen und verständlichen Code zu schreiben sowie praktische Erfahrung mit Frameworks wie Flask und der Zusammenarbeit an einem gemeinsamen Softwareprojekt zu sammeln.

Besonders interessant an DealHive finde ich, dass wir eine Plattform entwickeln, die technische Umsetzung mit einer konkreten Produktidee und echten Nutzeranforderungen verbindet.

---

## Eidesstattliche Erklärung (Stand 17.05.2026)

**[Matthieu Weinlein, Matrikelnr.: 77211933341]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| #  | My contribution                                                               | Why I am proud of it                                                                                                                                                                                                                          | Which challenge I overcame                                                                                                                                                                                                                               |
| :- | :---------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | Profilbereich mit vollständiger Profilanzeige und Profilbearbeitung umgesetzt | Dadurch wurde der Nutzerbereich der App deutlich vollständiger. Die Profilseite zeigt jetzt nicht nur einfache Session-Daten, sondern vollständige Nutzerdaten aus der Datenbank. Außerdem können Nutzer ihre Daten bearbeiten und speichern. | Die Herausforderung war, Session-Daten, Datenbankfunktionen, Flask-Routen und HTML-Templates korrekt miteinander zu verbinden. Besonders wichtig war, die Daten über `session["user_id"]` aus der Datenbank zu laden und Änderungen wieder zu speichern. |
| 2  | Creator Dashboard und Hive-Zuordnung verbessert                               | Dadurch kann ein Creator seine eigenen Hives im Dashboard sehen und Aktionen wie Details ansehen, Hive bearbeiten oder neuen Hive erstellen nutzen. Außerdem wurden Links in Buttons umgewandelt, damit die Oberfläche einheitlicher wirkt.   | Die Herausforderung war, zu verstehen, dass Hives nicht einfach global angezeigt werden sollen, sondern über die Tabelle `user_hives` einem Nutzer mit einer bestimmten Rolle zugeordnet werden.                                                         |
| 3  | Data-Model-Dokumentation aktualisiert                                         | Dadurch ist die technische Struktur der Datenbank besser nachvollziehbar. Die Dokumentation beschreibt jetzt die aktuellen Tabellen, Spalten, Beziehungen und wichtigen Funktionen aus `database.py`.                                         | Die Herausforderung war, die große und gewachsene `database.py` verständlich zusammenzufassen, ohne einfach den kompletten Code zu kopieren.                                                                                                             |

## Contributions

| Contribution                                                              | Proof, e.g., git commits                                                                                                                                        | Sources used                                                              |
| :------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------ |
| Profilseite in das gemeinsame Layout eingebunden                          | Branch `feature/matthieu-profile-edit`, Commit `Update profile page layout`, Datei `templates/profile.html`                                                     | FSWD-Template, bestehendes `layout.html`, eigene Umsetzung                |
| Vollständige Profildaten aus der Datenbank angezeigt                      | Branch `feature/matthieu-profile-edit`, Commit `Show full user profile data`, Dateien `user_routes.py`, `profile.html`, `database.py`                           | Eigene Umsetzung, Teamabstimmung                                          |
| Datenbankfunktion zum Laden eines Nutzers per ID ergänzt                  | Commit `Add user lookup by id`, Funktion `get_user_by_id(user_id)` in `database.py`                                                                             | Bestehende Datenbankstruktur, eigene Umsetzung                            |
| Profilbearbeitung umgesetzt                                               | Commits `Add user profile update function`, `Add profile edit form`, `Connect profile edit route`, Dateien `database.py`, `user_routes.py`, `edit_profile.html` | Flask-Dokumentation aus dem Kurs, eigene Tests, ChatGPT als Unterstützung |
| Profil-Aktionen als Buttons dargestellt                                   | Commit `Use buttons for profile actions`, Dateien `profile.html`, `edit_profile.html`                                                                           | Bestehendes Button-Styling aus `layout.html`, Feedback von Daniil         |
| Creator Dashboard weiter verbessert                                       | Branch `feature/matthieu-profile-edit`, Datei `creator_dashboard.html`                                                                                          | Teamfeedback, bestehende Creator-Routen                                   |
| Links im Creator Dashboard in Buttons umgewandelt                         | Commit `Use buttons in creator dashboard`, Datei `creator_dashboard.html`                                                                                       | Feedback von Daniil, bestehendes Layout                                   |
| Creator-Hive-Zuordnung über `user_hives` genutzt                          | Creator Dashboard und Datenbankfunktionen in `database.py`                                                                                                      | Teamabstimmung, bestehendes Datenmodell                                   |
| Data-Model-Dokumentation aktualisiert                                     | Branch `feature/matthieu-data-model`, Commit `Document database model`, Datei `docs/02-data-model.md`                                                           | Aktuelle `database.py`, Teamfeedback von Daniil                           |
| Datenbanktabellen dokumentiert                                            | `docs/02-data-model.md` mit Tabellen `users`, `hives`, `user_hives`, `hive_tiers`, `messages`                                                                   | Aktuelle Datenbankstruktur                                                |
| Datenbankfunktionen dokumentiert                                          | Funktionsübersicht in `docs/02-data-model.md`                                                                                                                   | Aktuelle `database.py`, eigene Zusammenfassung                            |
| Mitarbeit an der Ausarbeitung des DealHive-Konzepts                       | Dokumentation in [Value Proposition](../01-value-proposition.md) und Bereichen der Product Discovery                                                            | Teamdiskussionen, eigene Ideen, bestehender Value Proposition Canvas      |
| Mitarbeit an der Strukturierung der Projektdokumentation im FSWD-Template | Dateien im `/docs`-Ordner                                                                                                                                       | FSWD-App-Template des Kurses                                              |
| Pflege der eigenen Contribution-Seite                                     | Diese Datei                                                                                                                                                     | FSWD Contribution Template                                                |

---

## Design Decisions

### Design Decision 1: Separate Verbindungstabelle zwischen Nutzern und Hives

Wir haben uns entschieden, die Beziehung zwischen Nutzern und Hives über die Tabelle `user_hives` abzubilden.

**Begründung:**

Ein Hive kann einen Creator und mehrere Buyer haben. Gleichzeitig kann ein Nutzer an mehreren Hives beteiligt sein oder mehrere Hives erstellen. Deshalb ist eine separate Verbindungstabelle flexibler als eine direkte Speicherung in der Tabelle `hives`.

**Betrachtete Alternative:**

Eine Alternative wäre gewesen, eine Spalte `creator_id` direkt in der Tabelle `hives` zu speichern. Das hätte aber nur den Creator abgebildet und nicht sauber unterstützt, dass mehrere Buyer einem Hive beitreten können.

**Finale Entscheidung:**

Wir verwenden `user_hives` mit den Spalten `user_id`, `hive_id`, `relation_type` und `quantity`.

Dadurch kann gespeichert werden, ob ein Nutzer mit einem Hive als `creator` oder als `buyer` verbunden ist. Zusätzlich kann über `quantity` gespeichert werden, wie viele Einheiten ein Buyer bestellen möchte.

---

### Design Decision 2: Eigene Tabelle für Preisstaffeln

Wir haben uns entschieden, Preisstaffeln in einer eigenen Tabelle namens `hive_tiers` zu speichern.

**Begründung:**

Ein Hive kann mehrere Rabattstufen haben. Jede Rabattstufe besteht aus einer Mindestmenge und einem Rabatt in Prozent. Eine eigene Tabelle macht diese Struktur übersichtlicher und besser erweiterbar.

**Betrachtete Alternative:**

Eine Alternative wäre gewesen, die Preisstaffeln als Dictionary oder JSON-ähnliche Struktur zu speichern. Das wäre aber schwieriger abzufragen, zu ändern und im relationalen Datenmodell zu erklären.

**Finale Entscheidung:**

Wir verwenden `hive_tiers` mit den Spalten `hive_id`, `threshold_quantity` und `discount_percent`.

Der Grundpreis wird in `hives.base_price` gespeichert. Der aktuelle Preis kann dann aus dem Grundpreis, der aktuellen Bestellmenge und der passenden Rabattstufe berechnet werden.

---

## AI Directory

| #  | AI Tool | Purpose of Use                                                                 | Affected Sections (Code + Docs)                                                                | Remarks, Procedure, Prompts                                                                                                                                     |
| :- | :------ | :----------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 01 | ChatGPT | Unterstützung beim Formulieren und Strukturieren von Dokumentationstexten      | Teile der Dokumentation im `/docs`-Ordner                                                      | Die Inhalte wurden überprüft, angepasst und nicht unverändert übernommen.                                                                                       |
| 02 | ChatGPT | Unterstützung bei Ideenfindung für UI, Plattformstruktur und Value Proposition | Product Discovery, Value Proposition                                                           | Nutzung als Unterstützung bei Brainstorming und Formulierung. Die finalen Inhalte wurden manuell angepasst.                                                     |
| 03 | ChatGPT | Unterstützung bei Git-, Markdown- und Template-Fragen                          | Arbeit im FSWD-Template und Dokumentationsstruktur                                             | Nutzung als technische Hilfe bei Aufbau und Strukturierung des Projekts.                                                                                        |
| 04 | ChatGPT | Unterstützung bei der sprachlichen Überarbeitung einzelner Texte               | Contributions und Projektdokumentation                                                         | Nutzung als Formulierungshilfe für verständlichere und professionellere Texte.                                                                                  |
| 05 | ChatGPT | Unterstützung bei Coding-Fragen und Fehlersuche                                | `database.py`, `user_routes.py`, `profile.html`, `edit_profile.html`, `creator_dashboard.html` | Nutzung als Schritt-für-Schritt-Hilfe bei Flask-Routen, SQLite-Funktionen, Templates und Fehlermeldungen. Code wurde manuell eingefügt, getestet und angepasst. |
| 06 | ChatGPT | Unterstützung bei der Dokumentation des Datenmodells                           | `docs/02-data-model.md`                                                                        | Nutzung zur Strukturierung der Tabellen- und Funktionsübersicht. Inhalte wurden mit der aktuellen `database.py` abgeglichen und manuell übernommen.             |
| 07 | ChatGPT | Unterstützung beim Überarbeiten der eigenen Contribution-Seite                 | `docs/contributions/matthieu-weinlein.md`                                                      | Nutzung als Formulierungshilfe für meine eigenen Beiträge, Design Decisions und den AI-Directory-Abschnitt. Inhalte wurden geprüft und angepasst.               |