---
title: Design Decisions
nav_order: 5
has_children: true
---

# Design Decisions

In diesem Bereich dokumentieren wir die wichtigsten Design Decisions (Architekturentscheidungen) für DealHive.

DealHive ist eine Flask Web-App für Creator-basierten Gruppenkauf im Bereich Board Games, TTRPGs, Tabletop-Spiele und Zubehör. Die App ist bewusst als kleines, fokussiertes MVP (Minimum Viable Product) konzipiert und nicht als vollwertiger, komplexer Marktplatz.

| ID | Decision | Status | Main files |
| --- | --- | --- | --- |
| DD-01 | Creator erstellen Hives, Käufer treten ihnen bei | Decided | `hives.py`, `creator_routes.py`, templates |
| DD-02 | Buyer- und Creator-Rollen über Session steuern | Decided | `user_routes.py`, `sidebar.html`, `creator_routes.py` |
| DD-03 | DB-Zugriffe direkt über SQLite `execute` | Decided | `database.py` |
| DD-04 | User-Hive-Beziehungen über `user_hives` abbilden | Decided | `database.py`, `hives.py`, `creator_routes.py` |
| DD-05 | Dynamische Formularzeilen – Jinja2-Schleife vs. JS | Decided | `database.py`, `create_hive.html` |
| DD-06 | Flask-Routen nach Verantwortlichkeit aufteilen | Decided | `app.py`, `user_routes.py`, `hives.py`, `creator_routes.py` |
| DD-07 | Gemeinsames Jinja-Layout und Sidebar nutzen | Decided | `layout.html`, `sidebar.html` |
| DD-08 | Chat-MVP – Simples HTML-Formular vs. WebSockets | Decided | `hives.py`, `chat.html`, `my_chats.html` |
| DD-09 | Headless API für Hives bereitstellen (`/api/hives`) | Decided | `hives.py` |
| DD-10 | Daten richtig speichern vs. nur in einer Python-Liste | Decided | `app.py`, `database.py` |
| DD-11 | Formular-Validierung – Optionale Rabatte abfangen | Decided | `creator_routes.py`, `database.py` |
| DD-12 | Käuferliste absichern – Schutz gegen URL-Tricks | Decided | `creator_routes.py` |