---
title: DD-12
parent: Design Decisions
---

{: .no_toc }
# 12: Käuferliste absichern, Schutz gegen URL Tricks

## Meta

Status
: **Decided**

Updated
: 23-Jun-2026

## Problem Statement

Über die neue Route `/creator/hives/<int:hive_id>/buyers` können Creator die Namen und Adressen ihrer Käufer sehen. Weil die `hive_id` einfach als Zahl oben in der Browser-Zeile steht, könnte man die Zahl dort manuell ändern (z. B. von 3 auf 4) und so die privaten Bestelldaten von völlig fremden Hives ausspionieren. 

Wie machen wir diese sensiblen Daten wirklich sicher?

## Decision

Die Route wird im Backend strikt abgesichert. Flask prüft nicht nur, ob man generell als Creator eingeloggt ist, sondern vergleicht über die Funktion `get_hive_creator_id(hive_id)` die echte User-ID des Hive Besitzers aus der Datenbank mit der eigenen Session. Passt das nicht zusammen, blockiert der Server den Zugriff sofort und leitet um.

*Decision was taken by:* Darian Omorowa

## Regarded options

We regarded two alternative options:

+ Den Button zur Käuferliste im HTML für fremde Leute einfach ausblenden
+ Den Zugriff direkt im Python backend über einen Datenbankabgleich blockieren

| Kriterium | UI-Verstecken | Backend-Absicherung |
| --- | --- | --- |
| **Sicherheit** | ❌ Katastrophe. Wer die URL rät, sieht alles | ✔️ Sicher. Manuelle URL-Eingabe wird hart geblockt |
| **Datenschutz** | ❌ Hohes Risiko, dass Adressdaten geleakt werden | ✔️ Adressen und Namen sind zuverlässig geschützt |