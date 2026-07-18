---
title: DD-10-sqlite-storage
parent: Design Decisions
nav_order: 10
---

{: .no_toc }

# 10: Daten richtig speichern vs. nur in einer Pythonliste

## Meta

Status
: **Decided**

Updated
: 23-Jun-2026

## Problem Statement

Als ich das erste Erstellungsformular gebaut habe, mussten die Daten irgendwo gespeichert werden. Für den Anfang hat eine einfache Pythonliste (`simulierte_hives = []`) gereicht. Das Problem: Sobald der Server neu startet, sind alle Hives weg. Außerdem können wir so später keine echten Käufer mit den Hives verknüpfen.

Wie setzen wir die Datenspeicherung für die Hives so auf, dass sie zukunftssicher ist?

## Decision

Die temporäre Liste fliegt raus. Neue Hives werden ab jetzt direkt richtig in unserer SQLite Datenbank gespeichert. Über die neue Zwischentabelle `user_hives` wird der Hive auch gleich fest mit der User-ID des Creators verknüpft, der ihn angelegt hat.

*Decision was taken by:* Darian Omorowa

## Regarded options

We regarded two alternative options:

+ Die Daten einfach weiter in einer Pythonliste im Arbeitsspeicher behalten
+ Direkt Tabellen in SQLite anlegen und die Verknüpfung über eine Zwischentabelle lösen

| Kriterium | Python-Liste | SQLite + Zwischentabelle |
| --- | --- | --- |
| **Aufwand** | ✔️ Super schnell gebaut, man spart sich SQL-Befehle | ❌ Man muss Tabellen und Cursor-Logik in Python schreiben |
| **Nachvollziehbarkeit** | ❌ Nach jedem Server  Neustart ist alles gelöscht | ✔️ Permanent! die Daten bleiben in der Datenbank |
| **Erweiterbarkeit** | ❌ Käufer können dem Hive später nicht richtig beitreten | ✔️ Perfekt, um später unendlich viele Käufer zuzuordnen |