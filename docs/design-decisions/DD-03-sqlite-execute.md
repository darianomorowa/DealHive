---

title: DD-03
parent: Design Decisions
nav_order: 3
------------

{: .no_toc }

# 03: DB-Zugriffe

## Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 23-Jun-2026

## Direkt zum Punkt

Die entscheidung fiel uns sehr leicht, weil Herr Eck gesagt hat, dass wir execute nutzen sollen, anstatt von db.query. Aber wenn ich selber nachdenken müsste, hätte ich wahrscheinlich in Hinsicht auf unsere Projektgröße genau die selbe Wahl getroffen, weil:

* wir direkt sehen, welches SQL ausgeführt wird
* wir keine zusätzliche ORM-Struktur erklären müssen
* SQLite für unser Projekt völlig ausreicht
* die Datenbanklogik dadurch einfacher nachvollziehbar bleibt
* es in der mündlichen Prüfung weniger „Magie im Hintergrund“ gibt
* wir schneller erkennen, welche Tabelle gerade gelesen oder geändert wird
