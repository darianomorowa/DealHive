---
title: DD-11-backend-validation
parent: Design Decisions
nav_order: 11
---

{: .no_toc }

# 11: Formular-Validierung - Optionale Rabatte abfangen

## Meta

Status
: **Decided**

Updated
: 23-Jun-2026

## Problem Statement

Herr Prof. Dr. Eck meinte im Feedback, dass die Rabattstufen komplett optional sein sollen, damit man einen Hive auch ohne Rabatt erstellen kann. Wenn ein Creator die Felder aber einfach leer lässt, schickt der Browser leere Strings ans Backend. Das führt im Code beim Umwandeln in Zahlen zu Fehlern (`ValueError`) und crasht die Datenbank. 

Wie verhindern wir Abstürze, ohne den Creator zum Ausfüllen der Felder zu zwingen?

## Decision

Ich habe das Backend so umgebaut, dass wir leere Eingaben tolerieren. Eine Schleife (`for i in range(len(thresholds))`) geht durch alle Felder durch und checkt, ob wirklich Zahlen drinstehen. Wenn eine Zeile leer gelassen wurde, ignorieren wir sie beim Speichern einfach, statt einen Fehler zu werfen.

*Decision was taken by:* Darian Omorowa

## Regarded options

We regarded two alternative options:

+ Die HTML-Felder mit `required` zu Pflichtfeldern machen
+ Die Felder optional lassen und leere Eingaben im Backend per if-Abfrage aussortieren

| Kriterium | Pflichtfelder | Backend-Filter |
| --- | --- | --- |
| **Dozenten-Feedback** | ❌ Verstößt gegen die Vorgabe von Herrn Prof. Dr. Eck | ✔️ Setzt das Feedback (optional) perfekt um |
| **Sicherheit im Code** | ✔️ Verhindert leere Werte hart durch HTML-Zwang | ✔️ Fängt leere Werte im Code sauber und unsichtbar ab |
| **Nutzerfreundlichkeit** | ❌ Nervig, weil man zu Rabatten gezwungen wird | ✔️ Super, Rabatte sind möglich, aber freiwillig |