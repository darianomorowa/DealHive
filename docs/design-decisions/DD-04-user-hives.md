---
title: DD-04-user-hives
parent: Design Decisions
nav_order: 4
---

{: .no_toc }

# 04: User-Hive-Beziehungen über user_hives abbilden

## Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 23-Jun-2026

## Problemstellung

In DealHive reicht es nicht aus, Nutzer und Hives getrennt zu speichern. Wir müssen auch wissen, welcher Nutzer mit welchem Hive verbunden ist.

Dabei gibt es unterschiedliche Fälle:

* ein Creator erstellt und verwaltet einen Hive
* ein Käufer tritt einem Hive bei
* ein Käufer tritt mit einer bestimmten Menge bei
* ein User kann grundsätzlich sowohl Creator als auch Käufer sein

Eine einfache Spalte wie `creator_id` in der Tabelle `hives` hätte nur den Creator abgebildet. Für Käufer-Beitritte und Mengenangaben hätten wir dann trotzdem eine zusätzliche Struktur gebraucht. Das hätte sich schnell wie nachträglich drangeschraubt angefühlt.

## Entscheidung

Wir haben entschieden, eine eigene Beziehungstabelle `user_hives` zu nutzen.

Diese Tabelle verbindet Nutzer und Hives miteinander. Zusätzlich speichert sie über `relation_type`, welche Beziehung besteht, zum Beispiel `creator` oder `buyer`. Über `quantity` wird gespeichert, mit welcher Menge ein Käufer einem Hive beitritt.

Vereinfacht sieht die Idee so aus:

```sql
user_id
hive_id
relation_type
quantity
```

Dadurch kann die App besser abbilden, was fachlich wirklich passiert. Ein Hive gehört nicht einfach nur zu irgendeinem Nutzer. Stattdessen können Nutzer auf unterschiedliche Weise mit einem Hive verbunden sein.

Das ist besonders wichtig für das Creator Dashboard und für den Beitrittsprozess. Creator sehen ihre eigenen Hives, Käufer können Hives beitreten und die gesammelte Nachfrage kann über die Menge erhöht werden.

## Betrachtete Optionen

| Kriterium                      | `creator_id` direkt in `hives` | Eigene Tabelle `user_hives`       | Separate Tabellen für Creator und Buyer |
| ------------------------------ | ------------------------------ | --------------------------------- | --------------------------------------- |
| **Flexibilität**               | Deckt nur Creator gut ab       | Deckt Creator und Buyer ab        | Möglich, aber aufwendiger               |
| **Mengenangabe beim Beitritt** | Nicht gut geeignet             | Direkt über `quantity` möglich    | Möglich, aber verteilt                  |
| **Verständlichkeit**           | Am Anfang einfach              | Etwas mehr Struktur, aber logisch | Mehr Tabellen zu erklären               |
| **Projektgröße**               | Für unseren Fall zu knapp      | Passt gut                         | Eher zu groß                            |
| **Prüfungserklärung**          | Schwächer bei Käuferlogik      | Gut am Datenmodell erklärbar      | Könnte unnötig kompliziert wirken       |

Wir haben uns für `user_hives` entschieden, weil diese Tabelle Creator-Zuordnung, Käufer-Beitritte und Mengenangaben an einer zentralen Stelle speichert. Das Datenmodell bleibt dadurch flexibler, ohne für unser Projekt zu groß zu werden.
