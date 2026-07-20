---
title: Haya Al-Abbasi
parent: Individual Contributions
nav_order: 3
---

{: .no_toc }

# Haya Al-Abbasi

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

---

## Meta-Goals

### Target grade

Meine Zielnote für dieses Modul ist **1,0**.

### Personal goals

Meine persönlichen Ziele in diesem Modul sind, meine Fähigkeiten im Bereich UI/UX-Design und Product Discovery weiterzuentwickeln sowie besser zu verstehen, wie digitale Plattformen nutzerfreundlich und sinnvoll aufgebaut werden.

Außerdem möchte ich lernen, wie man Ideen im Team entwickelt, strukturiert ausarbeitet und gemeinsam in ein funktionierendes Produktkonzept überführt.

Das Spannende an DealHive ist, dass wir nicht nur eine technische Plattform entwickeln, sondern ein Konzept mit realem Nutzen für Käufer und Creator gestalten.

---

## Eidesstattliche Erklärung (Stand 20.07.2026)

**[Haya Al-Abbasi, Matrikelnr.: 77211974821]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten, einschließlich KI-generierter Inhalte, ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| # | My contribution | Why I am proud of it | Which challenge I overcame |
| :- | :-- | :-- | :-- |
| 1 | Implementierung des Buyer-Flows „Meine Hives“ | Käufer können nach dem Beitritt ihre eigenen Hives übersichtlich verwalten und wiederfinden. | Die Herausforderung war, neue Routen, Templates und bestehende Datenbankfunktionen sauber miteinander zu verbinden. |
| 2 | Absicherung und Verbesserung des Hive-Beitritts | Der Join-Prozess wurde durch serverseitige Validierung und bessere Nutzerführung robuster gemacht. | Die Herausforderung war, Eingaben aus Formularen sicher zu verarbeiten und fehlerhafte Mengenangaben im Backend abzufangen. |
| 3 | Umsetzung von Sicherheitsverbesserungen durch Passwort-Hashing und Eingabevalidierung | Die Anwendung speichert Passwörter sicher und verarbeitet kritische Nutzereingaben robuster. | Die Herausforderung war, bestehende Authentifizierungs- und Join-Funktionen zu erweitern, ohne bestehende Teamfunktionalitäten zu beeinträchtigen. |

---

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Implementierung der Route `/my-hives` für eingeloggte Käufer | Commit `Added buyer my-hives flow`, Datei `user_routes.py` | Bestehende Datenbankfunktionen, Teamarchitektur |
| Erstellung der Seite `my_hives.html` zur Anzeige beigetretener Hives | Commit `Added buyer my-hives flow`, Datei `templates/my_hives.html` | Vorhandenes Layout (`layout.html`), Teamdesign |
| Erweiterung der Sidebar um den Menüpunkt „Meine Hives“ | Datei `templates/partials/sidebar.html` | Bestehende Navigationsstruktur |
| Verbesserung der Hive-Beitrittsbestätigung inkl. Hive-Name und Nutzerfeedback | Datei `templates/join_confirm.html` | Bestehender Buyer-Flow |
| Nutzung und Integration der bestehenden Datenbanklogik für Hive-Zuordnungen und Rückmeldung über erfolgreiche Beitritte (`relation_was_created`) | Datei `database.py`, Integration im Buyer-Flow | Bestehende Datenbankstruktur |
| Integration und Konfliktlösung beim Zusammenführen des Branches | Git-Historie, Rebase- und Merge-Prozess während der Feature-Integration | Git, GitHub, Teamarbeit |
| Passwort-Hashing für Registrierung und Login vervollständigt | Commit `Passwort-Hashing vervollständigt`, Dateien `user_routes.py`, `database.py`, `test_database.py` | Werkzeug Security Funktionen (`generate_password_hash`, `check_password_hash`) |
| Serverseitige Validierung der Hive-Beitrittsmenge ergänzt | Commit `Validate hive join quantity input`, Datei `hives.py`, Route `/hives/<int:hive_id>/join` | Flask Request-Verarbeitung und Backend-Validierung |
| README-Dokumentation zu Demo-Zugängen und API-Nutzung verbessert | Commit `Improve README documentation for demo access and API` | Projektdokumentation und eigene Überarbeitung |
| Eigene Contribution-Seite gepflegt | Diese Datei | FSWD Contribution Template |

---

## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :- | :-- | :-- | :-- | :-- |
| 01 | ChatGPT | Unterstützung beim Strukturieren und Formulieren von Dokumentationstexten | Contributions, Reflection | Inhalte wurden geprüft und angepasst. |
| 02 | ChatGPT | Unterstützung bei UI-/UX-Ideen und Brainstorming | Product Discovery, UI-Screens | Nutzung als Ideengeber und Formulierungshilfe. |
| 03 | Claude (claude.ai) | Unterstützung bei konzeptionellen Ideen und Textverbesserung | Contributions, Product Discovery | Inhalte wurden manuell überarbeitet und angepasst. |
| 04 | ChatGPT | Unterstützung bei Git-, GitHub- und Template-Fragen | Arbeit mit Branches, Commits und Dokumentationsstruktur | Nutzung als Schritt-für-Schritt-Hilfe. Befehle wurden manuell ausgeführt und kontrolliert. |
| 05 | ChatGPT | Unterstützung bei Implementierung und Debugging des Buyer-Flows | `user_routes.py`, `database.py`, `hives.py`, `join_confirm.html`, `my_hives.html` | Nutzung zur Fehlersuche, Git-Konfliktlösung und Implementierung. Änderungen wurden manuell geprüft und übernommen. |
| 06 | ChatGPT | Unterstützung bei Passwort-Hashing, Validierung und Dokumentationsüberarbeitung | `user_routes.py`, `database.py`, `hives.py`, `README.md` | Nutzung zur Analyse von Fehlern und Verbesserungsvorschlägen. Änderungen wurden geprüft, angepasst und lokal getestet. |
