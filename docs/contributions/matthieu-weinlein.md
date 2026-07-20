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

Außerdem ist es mein Ziel, sauberen und verständlichen Code zu schreiben sowie praktische Erfahrung mit dem Framework Flask und der Zusammenarbeit an einem gemeinsamen Softwareprojekt zu sammeln.

Besonders interessant an DealHive finde ich, dass wir eine Plattform entwickeln, die eine technische Umsetzung mit einer konkreten Produktidee und echten Nutzeranforderungen verbindet.

---

## Eidesstattliche Erklärung (Stand 19.07.2026)

**[Matthieu Weinlein, Matrikelnr.: 77211933341]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten – einschließlich KI-generierter Inhalte – ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit „nicht ausreichend“ führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| # | My contribution | Why I am proud of it | Which challenge I overcame |
| :- | :----------- | :------------------------- | :------------------------------------------ |
| 1 | Profilbereich mit vollständiger Profilanzeige, Profilbearbeitung und Validierung umgesetzt | Dadurch wurde der Nutzerbereich der Anwendung deutlich erweitert. Nutzer können ihre vollständigen Profildaten aus der Datenbank anzeigen, bearbeiten und speichern. Zusätzlich werden ungültige Eingaben sowohl im Formular als auch serverseitig überprüft. | Die Herausforderung bestand darin, Session-Daten, Datenbankfunktionen, Flask-Routen und HTML-Templates korrekt miteinander zu verbinden. Außerdem musste verhindert werden, dass unvollständige oder ungültige Daten in der Datenbank gespeichert werden. |
| 2 | Creator Dashboard und Zuordnung zwischen Nutzern und Hives umgesetzt und verbessert | Creator können ihre zugeordneten Hives im Dashboard sehen und die vorhandenen Aktionen über eine einheitliche Benutzeroberfläche aufrufen. Durch die Verwendung von Buttons und die korrekte Hive-Zuordnung ist das Dashboard übersichtlicher und benutzerfreundlicher geworden. | Die Herausforderung bestand darin, die Beziehung zwischen Nutzern und Hives über die Verbindungstabelle `user_hives` korrekt abzubilden. Dabei musste berücksichtigt werden, ob ein Nutzer einem Hive als `creator` oder als `buyer` zugeordnet ist. |
| 3 | Datenmodell und Datenbankfunktionen dokumentiert | Die Dokumentation bildet die aktuelle technische Struktur der Datenbank ab und erklärt die wichtigsten Tabellen, Beziehungen und Funktionen. Dadurch ist das Datenmodell auch für andere Teammitglieder besser nachvollziehbar. | Die Herausforderung bestand darin, die gewachsene Datei `database.py` verständlich zusammenzufassen, ohne lediglich den vollständigen Quellcode zu kopieren. Die Informationen mussten strukturiert und mit dem tatsächlichen Stand der Implementierung abgeglichen werden. |

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :------ | :-------------------------- | :----------------- |
| Grundstruktur der persönlichen Contribution-Seite erstellt | Commit `Individual Contributions Matthieu`, Datei `docs/contributions/matthieu-weinlein.md` | FSWD Contribution Template, eigene Inhalte |
| Dokumentation des Datenmodells begonnen | Commit `Add data model documentation`, Datei `docs/02-data-model.md` | Bestehende Datenbankstruktur, eigene Ausarbeitung |
| Creator Dashboard mit User-Hive-Zuordnung umgesetzt | Commit `Add creator dashboard with user hive mapping`, Dateien `creator_dashboard.html`, `user_routes.py` und `database.py` | Bestehendes Datenmodell, Teamabstimmung, eigene Umsetzung |
| Profilseite in das gemeinsame Layout eingebunden | Commit `Update profile page layout`, Datei `templates/profile.html` | FSWD-Template, bestehendes `layout.html`, eigene Umsetzung |
| Datenbankfunktion zum Laden eines Nutzers über seine ID ergänzt | Commit `Add user lookup by id`, Funktion `get_user_by_id(user_id)` in `database.py` | Bestehende Datenbankstruktur, eigene Umsetzung |
| Vollständige Profildaten aus der Datenbank auf der Profilseite angezeigt | Commit `Show full user profile data`, Dateien `user_routes.py`, `profile.html` und `database.py` | Bestehende Flask-Struktur, Teamabstimmung, eigene Umsetzung |
| Datenbankfunktion zum Aktualisieren eines Nutzerprofils umgesetzt | Commit `Add user profile update function`, Funktion in `database.py` | Bestehende Datenbankstruktur, eigene Umsetzung |
| Formular zur Bearbeitung des Profils erstellt | Commit `Add profile edit form`, Datei `templates/edit_profile.html` | Bestehende Templates, HTML-Formulare, eigene Umsetzung |
| Flask-Route für die Profilbearbeitung angebunden | Commit `Connect profile edit route`, Datei `user_routes.py` | Flask-Kursmaterialien, bestehende Routenstruktur, eigene Tests |
| Profilaktionen als Buttons dargestellt | Commit `Use buttons for profile actions`, Dateien `profile.html` und `edit_profile.html` | Bestehendes Button-Styling, Feedback von Daniil |
| Links im Creator Dashboard durch Buttons ersetzt | Commit `Use buttons in creator dashboard`, Datei `creator_dashboard.html` | Bestehendes Layout, Teamfeedback |
| Datenmodell vollständig dokumentiert und aktualisiert | Commit `Document database model`, Datei `docs/02-data-model.md` | Aktuelle `database.py`, bestehende Tabellen und Funktionen |
| Eigene Contribution-Seite erweitert und aktualisiert | Commit `Update Matthieu individual contribution`, Datei `docs/contributions/matthieu-weinlein.md` | Eigene Git-Historie, FSWD Contribution Template |
| Datum der eidesstattlichen Erklärung aktualisiert | Commit `Update declaration date`, Datei `docs/contributions/matthieu-weinlein.md` | Eigene Dokumentation |
| Serverseitige Validierung für Profiländerungen ergänzt | Commit `Add server-side validation for profile updates`, Datei `user_routes.py` | Flask-Kursmaterialien, eigene Validierungslogik und Tests |
| Profilvalidierung und Navigation verbessert | Commit `Improve profile validation and navigation`, Dateien `user_routes.py` und `edit_profile.html` | Eigene Umsetzung, bestehende Profilfunktionen |
| Zulässige Werte für User-Hive-Beziehungen validiert | Commit `Validate user-hive relation types`, Datei `database.py` | Bestehendes Datenmodell, eigene Validierungslogik |
| Profilformular durch Autocomplete-Attribute und verbesserte PLZ-Eingabe optimiert |  Commit `Improve profile form accessibility and autocomplete`, Datei `templates/edit_profile.html` | HTML-Autocomplete-Attribute, bestehendes Formular, eigene Umsetzung |
| Mitarbeit an der Ausarbeitung des DealHive-Konzepts | Dokumentation in [Value Proposition](../01-value-proposition.md) und Bereichen der Product Discovery | Teamdiskussionen, eigene Ideen, bestehender Value Proposition Canvas |
| Mitarbeit an der Strukturierung der Projektdokumentation im FSWD-Template | Dateien im Verzeichnis `/docs` | FSWD-App-Template des Kurses |
| Pflege und abschließende Überarbeitung der persönlichen Contribution-Seite | Diese Datei | Eigene Git-Commits, Projektdokumentation und FSWD Contribution Template |

---

## Design Decisions

### Design Decision 1: Separate Verbindungstabelle zwischen Nutzern und Hives

Wir haben uns entschieden, die Beziehung zwischen Nutzern und Hives über die Tabelle `user_hives` abzubilden.

**Begründung:**

Ein Hive kann einen Creator und mehrere Buyer haben. Gleichzeitig kann ein Nutzer an mehreren Hives beteiligt sein oder mehrere Hives erstellen. Deshalb ist eine separate Verbindungstabelle flexibler als eine direkte Speicherung der Nutzerbeziehungen in der Tabelle `hives`.

**Betrachtete Alternative:**

Eine Alternative wäre gewesen, eine Spalte `creator_id` direkt in der Tabelle `hives` zu speichern. Dadurch hätte jedoch nur der Creator abgebildet werden können. Die Zuordnung mehrerer Buyer zu einem Hive wäre damit nicht ausreichend unterstützt worden.

**Finale Entscheidung:**

Wir verwenden die Tabelle `user_hives` mit den Spalten `user_id`, `hive_id`, `relation_type` und `quantity`.

Über `relation_type` kann gespeichert werden, ob ein Nutzer einem Hive als `creator` oder als `buyer` zugeordnet ist. Zusätzlich kann über `quantity` gespeichert werden, wie viele Einheiten ein Buyer bestellen möchte.

Damit keine ungültigen Zuordnungen gespeichert werden, werden die zulässigen Werte für `relation_type` zusätzlich in der Datenbanklogik validiert.

---

### Design Decision 2: Eigene Tabelle für Preisstaffeln

Wir haben uns entschieden, Preisstaffeln in einer eigenen Tabelle namens `hive_tiers` zu speichern.

**Begründung:**

Ein Hive kann mehrere Rabattstufen besitzen. Jede Rabattstufe besteht aus einer Mindestmenge und einem Rabatt in Prozent. Eine eigene Tabelle macht diese Struktur übersichtlicher, besser abfragbar und einfacher erweiterbar.

**Betrachtete Alternative:**

Eine Alternative wäre gewesen, die Preisstaffeln als Dictionary oder als JSON-ähnliche Struktur direkt in der Tabelle `hives` zu speichern. Dadurch wären einzelne Preisstaffeln jedoch schwieriger abzufragen, zu ändern und innerhalb eines relationalen Datenmodells abzubilden gewesen.

**Finale Entscheidung:**

Wir verwenden die Tabelle `hive_tiers` mit den Spalten `hive_id`, `threshold_quantity` und `discount_percent`.

Der Grundpreis wird in `hives.base_price` gespeichert. Der aktuelle Preis kann anschließend aus dem Grundpreis, der aktuellen Bestellmenge und der jeweils erreichten Rabattstufe berechnet werden.

---

## AI Directory

| # | AI Tool | Verwendungszweck | Betroffene Bereiche (Code und Dokumentation) | Anmerkungen, Vorgehen und Prompts |
| :- | :------ | :--------------- | :------------------------------------------- | :------------------------------- |
| 01 | ChatGPT | Unterstützung beim Formulieren und Strukturieren von Dokumentationstexten | Teile der Dokumentation im Verzeichnis `/docs` | Die vorgeschlagenen Inhalte wurden überprüft, sprachlich angepasst und nicht unverändert übernommen. |
| 02 | ChatGPT | Unterstützung bei der Ideenfindung für Benutzeroberfläche, Plattformstruktur und Value Proposition | Product Discovery und Value Proposition | Nutzung zur Unterstützung beim Brainstorming und bei der Formulierung. Die finalen Inhalte wurden manuell ausgewählt und angepasst. |
| 03 | ChatGPT | Unterstützung bei Git-, Markdown- und Template-Fragen | Arbeit mit Git, dem FSWD-Template und der Dokumentationsstruktur | Nutzung als technische Hilfe bei einzelnen Git-Befehlen sowie beim Aufbau und bei der Formatierung der Projektdokumentation. |
| 04 | ChatGPT | Unterstützung bei der sprachlichen Überarbeitung einzelner Texte | Contributions und weitere Bereiche der Projektdokumentation | Nutzung als Formulierungshilfe, um eigene Inhalte verständlicher und professioneller auszudrücken. |
| 05 | ChatGPT | Unterstützung bei Coding-Fragen und bei der Fehlersuche | `database.py`, `user_routes.py`, `profile.html`, `edit_profile.html` und `creator_dashboard.html` | Nutzung als schrittweise Hilfe bei Flask-Routen, SQLite-Funktionen, Session-Daten, serverseitiger Validierung, HTML-Formularen, Templates und Fehlermeldungen. Vorgeschlagener Code wurde manuell eingefügt, geprüft, getestet und bei Bedarf angepasst. |
| 06 | ChatGPT | Unterstützung bei der Dokumentation des Datenmodells | `docs/02-data-model.md` | Nutzung zur Strukturierung der Tabellen-, Beziehungs- und Funktionsübersicht. Die Inhalte wurden mit der aktuellen Datei `database.py` abgeglichen und manuell angepasst. |
| 07 | ChatGPT | Unterstützung bei der Überarbeitung der persönlichen Contribution-Seite | `docs/contributions/matthieu-weinlein.md` | Nutzung als Formulierungshilfe für eigene Beiträge, Design Decisions und den AI-Directory-Abschnitt. Die Vorschläge wurden überprüft, an den aktuellen Projektstand angepasst und eigenständig übernommen. |