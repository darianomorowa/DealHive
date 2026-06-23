---
title: DD-08
parent: Design Decisions
---

{: .no_toc }
# 08: Chat-MVP – Simples HTML-Formular vs. Live Chat mit WebSockets

## Meta

Status
: **Decided**

Updated
: 23-Jun-2026

## Problem Statement

Die App braucht ein ChatFeature, damit Käufer und Creator sich zu einem Hive absprechen können. Ein echter Live Chat mit WebSockets und viel JavaScript ist aber viel zu komplex und fliegt uns bei der lokalen Abgabe um die Ohren, wenn Skripte blockiert werden. 

Wie bauen wir einen simplen, aber komplett stabilen Chat?

## Decision

Wir bauen einen ganz einfachen 1 on 1 Chat (wie bei eBay Kleinanzeigen) komplett ohne JavaScript. 

Man schreibt eine Nachricht in ein normales HTML Formular, klickt auf Senden (POST-Request an den Server) und die Seite lädt einfach kurz neu, um die neue Nachricht anzuzeigen. Das reicht für unsere Zwecke völlig aus und stürzt garantiert nicht ab.

*Decision was taken by:* Darian Omorowa

## Regarded options

We regarded two alternative options:

+ Ein aufwendiger Live Chat mit WebSockets und JS Libraries
+ Ein ganz normales HTML Formular mit klassischer GET/POST Logik im Backend

| Kriterium | WebSockets / JS | Klassisch HTML / Flask |
| --- | --- | --- |
| **Stabilität** | ❌ Fehleranfällig, wenn JS lokal blockiert wird | ✔️ Läuft immer und überall (nativer Standard) |
| **Code-Komplexität** | ❌ Viel Zusatzaufwand, der vom Kern der App ablenkt | ✔️ Schlanke SQL-Tabelle (`messages`) reicht völlig |
| **Zweck für MVP** | ❌ Overengineered für eine simple Absprache | ✔️ Erfüllt den Zweck für die Kommunikation perfekt |