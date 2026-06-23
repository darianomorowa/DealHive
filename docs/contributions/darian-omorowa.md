---
title: Darian Omorowa
parent: Individual Contributions
nav_order: 2
---

{: .no_toc }
# Darian Omorowa

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

Meine persönlichen Ziele in diesem Modul sind, die Full-Stack-Grundstruktur zu verstehen und anwenden zu können (Python, Flask, SQLite, Jinja2), um eigenständig betriebswirtschaftliche Web-Applikationen konzipieren und entwickeln zu können.

Dabei möchte ich den gesamten Entwicklungsprozess verstehen, von der Idee bis zur lauffähigen Web-App, und nicht nur Code schreiben, sondern auch strategisch und produktseitig denken.

---

## Eidesstattliche Erklärung (Stand 23.06.2026)

**[Darian Omorowa, Matrikelnr.: 77211716160]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten, einschließlich KI-generierte Inhalte, ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

---

## Top-3 Contributions

| \# | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | **Dynamic Pricingsystem und Erstellungsablauf** | Ich habe das relationale Preismodell (`hive_tiers`) integriert, wodurch Rabattstufen dynamisch berechnet werden und vollkommen optional bleiben. | Die serverseitige Validierung so anzupassen, dass unvollständige Formulareingaben oder leere Rabattfelder nicht zu Datenbankabstürzen führen. |
| 2 | **1 zu 1 Kommunikationssystem (Chat MVP)** | Der Chat läuft robust im Hive Kontext (Kleinanzeigen Style) über reine HTML Formulare wwas die Abgabesicherheit komplett ohne JavaScript sichert. | Die saubere relationale Zuordnung und Filterung der Nachrichten nach `sender_id` und `receiver_id` direkt in den SQL abfragen. |
| 3 | **Entwicklung der Käuferübersicht für Creator** | Das Feature ermöglicht dem Creator erstmals eine tabellarische Übersicht über alle verbindlichen Käufer und Mengen direkt aus dem Dashboard heraus. | Die Implementierung einer strikten Autorisierungsprüfung im Backend, um **Cross user snooping+* auf fremde Käuferdaten über die URL zu blockieren. |

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| **Konzeption (Phase 1):** Mitarbeit an der Value Proposition Canvas für beide Customer Segments (Creator und Käufer). | Dokumentation in `docs/01-value-proposition.md`. | Teamdiskussionen, eigene Ideen, KI-Unterstützung für Formulierungen (siehe AI Directory, Eintrag #01 & #02). |
| **Konzeption (Phase 1):** Konzeptionelle Mitarbeit an der domainspezifischen Rollenstruktur der Plattform. | Dokumentation im Bereich Product Discovery. | Teamabstimmung, gemeinsame Ausarbeitung des Marktplatz-Konzepts (siehe AI Directory, Eintrag #01). |
| **Konzeption (Phase 1):** Konzeptionelle Definition des Target Scope und bewusste Eingrenzung der ersten App Version. | Dokumentation in den Projekt-Docs. | Gemeinsame Priorisierung im Team zur Sicherung des Happy Paths (siehe AI Directory, Eintrag #01). |
| **Sprint 1:** Erstellung des Basisformulars und der Route für neue Hives. | Commits `aaa7b94`, `ae4f540`, `7383039` in `templates/create_hive.html` und `app.py`. | Basis-Struktur aus dem HWR-FSWD-Kurs-Template, erweitert durch eigene Logik mit KI-Unterstützung (siehe AI Directory, Eintrag #04). |
| **Sprint 2:** Entwicklung des Chat MVP (1 on 1 Privatnachrichten) ohne JavaScript. | Commits `6c774a3`, `f7ce0cb`, `85057b7`, `16b1fe6` in `database.py` und `hives.py`. | sqLite Datenstruktur basierend auf der FSWD Kursseite, Codegenerierung über KI Unterstützung (siehe AI Directory, Eintrag #05). |
| **Sprint 3:** Einbau des dynamischen Pricing-Modells für optionale Rabattstufen. | Commits `c897ba`, `8fe6d13`, `efd463`, `8090c4` in `database.py` und `creator_routes.py`. | Konzeptionell basierend auf dem Dozenten-Feedback von Herrn Prof. Dr. Eck, Code-Anpassung mittels KI-Unterstützung (siehe AI Directory, Eintrag #06). |
| **Sprint 4 (Heutige Aufgabe):** Entwicklung der geschützten Käuferübersicht (Buyer Overview) im Dashboard. | Commits `494343f`, `4ec0503`, `3aa8ff2`, `40da155` in `database.py` und `creator_routes.py`. | Eigene Implementierung auf Basis der vorhandenen Dashboard-routen, Codereview und Absicherung durch Gemini (siehe AI Directory, Eintrag #07). |
| **Dokumentation:** Eigene Contribution Seite gepflegt. | Letzter Git commit in `docs/contributions/darian-omorowa.md`. | FSWD Contribution Vorlage der offiziellen Kursseite (https://hwrberlin.github.io/fswd/). |
---

## AI Directory

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :--     | :--            | :--                             | :--                         |
| 01  | Claude (claude.ai) | Sparringspartner für konzeptionelle Entscheidungen und Produktlogik. | Value Proposition, Rollenstruktur, Target Scope. | Nutzung als Denkpartner. **Prompts:** *"Wie grenze ich den Target Scope für die erste Version unserer App sinnvoll ein, um den Happy Path stabil zu halten?"* |
| 02  | Claude (claude.ai) | Sprachliche Formulierungshilfe für Dokumentationstexte. | Value Proposition, Contributions. | Nutzung als Formulierungshilfe. Die fachlichen Inhalte stammen aus der Gruppenarbeit. |
| 03  | Claude (claude.ai) | Unterstützung bei Git-Befehlen und Repository-Setup. | GitHub Repository, GitHub Pages. | Befehle wurden manuell ausgeführt. **Prompts:** *"Wie initialisiere ich ein Git-Repository über das Terminal und pushe den bestehenden Code auf GitHub?"* |
| 04  | Gemini (3.5 Flash) | Codegenerierung für das erste Grundgerüst der Hive-Erstellung. | `app.py`, `create_hive.html`. | Hilfestellung beim HTML-Formular (Commits `aaa7b94`, `7383039`). **Prompt:** *"Erstelle eine Flask Route unter /creator/hives/new und ein passendes Formular."* |
| 05  | Gemini (3.1 Pro) | Entwicklung der Logik für die relationale Speicherung im 1 on 1 Chat. | `database.py`, `hives.py`, `chat.html`. | Entwicklung der Tabellenstruktur (Commits `6c774a3`, `85057b7`). **Prompt:** *"Schreibe eine SQLite Struktur für private Nachrichten mit sender_id und receiver_id."* |
| 06  | Gemini (3.1 Pro) | Backend Validierung für die optionalen Rabattstufen. | `database.py`, `creator_routes.py`. | Absicherung der Preislogik (Commits `8fe6d13`, `8090c4`). **Prompt:** *"Wie passe ich die POST-Route so an, dass leere Rabattfelder im Formular keinen Datenbank-Fehler erzeugen?"* |
| 07  | Gemini (3.5 Flash) | Aufgabe vom 23.06.26: Datenbankabfrage und Sicherheitsprüfung für die Käuferübersicht. | `database.py`, `creator_routes.py`, `hive_buyers.html`. | Implementierung der Buyers Tabelle (Commits `494343f`, `4ec0503`). **Prompt:** *"Schreibe eine SQL abfrage get_buyers_for_hive und sichere die Route ab, damit nur der echte Creator Zugriff hat."* |