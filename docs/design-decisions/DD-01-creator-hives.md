---
title: DD-01-creator-hives
parent: Design Decisions
nav_order: 1
---

{: .no_toc }

# 01: Creator erstellen Hives, Käufer treten ihnen bei

## Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 23-Jun-2026

## Problemstellung

Am Anfang war DealHive noch breiter gedacht. Eine Idee war, dass Käufer eigene Anfragen erstellen und Creator darauf reagieren können.

Das hätte die App aber schnell zu komplex gemacht. Wir hätten dann Käuferanfragen, Creator-Antworten, mögliche Verhandlungen und mehr Statuslogik gebraucht. Aus einem klaren Gruppenkauf-Flow wäre ziemlich schnell ein Feature-Creep-Monster geworden.

Für unser Uni-Projekt wollten wir lieber einen kleineren, funktionierenden Kern bauen, den man gut testen und erklären kann.

## Entscheidung

Wir haben entschieden, dass nur Creator Hives erstellen. Käufer erstellen keine eigenen Anzeigen oder Anfragen, sondern treten bestehenden Hives bei.

Der Hauptflow ist dadurch klar:

1. Creator erstellt einen Hive.
2. Käufer sehen den Hive.
3. Käufer öffnen die Detailseite.
4. Käufer treten mit einer Menge bei.
5. Die Nachfrage steigt.
6. Rabattstaffeln können erreicht werden.

Diese Entscheidung reduziert den Umfang und macht DealHive stärker als Sammelkaufplattform erkennbar.

## Betrachtete Optionen

| Kriterium                       | Käufer erstellen Anfragen | Creator erstellen Hives | Beide Modelle                   |
| ------------------------------- | ------------------------- | ----------------------- | ------------------------------- |
| **Umfang**                      | Zu groß für den MVP       | Gut machbar             | Zu viele Flows                  |
| **Verständlichkeit**            | Schwerer zu erklären      | Sehr klarer Ablauf      | Schnell unübersichtlich         |
| **Implementierungsaufwand**     | Hoch                      | Mittel                  | Sehr hoch                       |
| **Passung zur Sammelkauf-Idee** | Möglich, aber indirekt    | Sehr passend            | Möglich, aber schwer konsistent |

Wir haben uns für Creator-erstellte Hives entschieden, weil dieser Ansatz die App fokussiert, verständlich und für den aktuellen Projektumfang realistisch hält.
