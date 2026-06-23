---
title: Value Proposition
nav_order: 1
---

{: .no_toc }
# Value Proposition

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## The Problem

In der Brettspiel-, TTRPG- und Tabletop-Community gibt es viele besondere Produkte, die nicht einfach als Massenware entstehen. Dazu gehören zum Beispiel handgemachte Würfelsets, Miniaturen, Dungeon-Terrain, Würfeltürme, Spielmatten, Kartenhalter oder Token-Sets.

Viele dieser Produkte werden von kleinen Creatorn, Künstlern, Handwerkern oder kleinen Shops hergestellt. Für diese Anbieter ist die Produktion oft schwer planbar. Material, Arbeitszeit und Vorbereitung fallen meistens an, bevor sicher ist, ob genug Käufer vorhanden sind.

Gleichzeitig sind solche Produkte für Käufer oft teuer oder schwer zu finden. Sammelbestellungen laufen häufig über Discord, Instagram, WhatsApp oder private Nachrichten. Dadurch wird schnell unübersichtlich, wie viele Personen bereits teilnehmen, ob die Mindestmenge erreicht wird und wann ein Rabatt möglich ist.

Das Kernproblem ist also die Koordination zwischen Angebot und Nachfrage. Anbieter brauchen genug Teilnehmer, bevor sich die Produktion lohnt. Käufer profitieren von besseren Preisen, wenn viele Personen gemeinsam teilnehmen.

## Our Solution

DealHive ist eine Web-App für Sammelkäufe im Bereich Brettspiele, TTRPGs, Tabletops und passendes Zubehör.

Creator können auf DealHive einen Sammelkauf erstellen. Dabei legen sie Informationen wie Produktname, Kategorie, Spielsystem, Material, Basispreis, Mindestteilnehmer, Deadline und Rabattstufen fest.

Käufer können offene Sammelkäufe entdecken, Details ansehen und einem Angebot beitreten. Die App zeigt transparent, wie viele Personen bereits teilnehmen, wie weit der Sammelkauf vom Produktionsstart entfernt ist und welche Rabattstufe als Nächstes erreicht werden kann.

Dadurch wird der Ablauf für beide Seiten klarer:

- Creator können Nachfrage besser einschätzen.
- Käufer können besondere Produkte entdecken.
- Sammelkäufe werden zentral und übersichtlich dargestellt.
- Mindestteilnehmer und Rabattstufen werden sichtbar.
- Der Prozess wirkt strukturierter als eine lose Sammelbestellung über Chatgruppen.

DealHive soll dabei nicht direkt ein kompletter Online-Shop mit Zahlung, Versand und Rechnungsstellung sein. Der Fokus der ersten Version liegt auf dem Kernprozess: Sammelkauf erstellen, entdecken, beitreten und Fortschritt verfolgen.

## Target User(s)

### Anbieter / Creator

Die erste Zielgruppe sind Creator, Künstler, Handwerker oder kleine Shops, die Produkte für Brettspiele, TTRPGs oder Tabletops herstellen.

Beispiele:

- Würfelmacher
- Miniaturenbemaler
- Terrainbauer
- Hersteller von Würfeltürmen
- kleine Shops für Tabletop-Zubehör
- Künstler mit limitierten Hobbyprodukten

Diese Nutzer möchten ihre Produkte sichtbar machen, Interesse sammeln und erst dann produzieren, wenn genug Nachfrage vorhanden ist.

### Käufer / Spieler

Die zweite Zielgruppe sind Käufer aus der Brettspiel-, TTRPG- und Tabletop-Community.

Beispiele:

- Dungeons-&-Dragons-Spieler
- Pathfinder-Spieler
- Warhammer-Spieler
- Brettspiel-Fans
- Sammler von Würfeln oder Miniaturen
- Spielleiter, die Zubehör für ihre Kampagnen suchen

Diese Nutzer möchten besondere Produkte finden und sich an Sammelkäufen beteiligen, ohne selbst eine ganze Gruppe organisieren zu müssen.

## Happy Path

Der Happy Path beschreibt den idealen Ablauf in der App.

1. Ein Creator meldet sich bei DealHive an.
2. Der Creator erstellt einen neuen Sammelkauf, zum Beispiel für ein handgemachtes Drachenwürfel-Set.
3. Der Creator gibt Produktinformationen ein, zum Beispiel Kategorie, Spielsystem, Material, Preis, Mindestteilnehmer und Rabattstufen.
4. Ein Käufer öffnet die Übersicht der Sammelkäufe.
5. Der Käufer findet das Drachenwürfel-Set und öffnet die Detailseite.
6. Auf der Detailseite sieht der Käufer Beschreibung, Creator, Preis, Teilnehmerstand, Produktionsziel und Rabattstufen.
7. Der Käufer tritt dem Sammelkauf bei.
8. Die Teilnehmerzahl steigt.
9. Der Käufer kann den Sammelkauf später unter „Meine Hives“ verfolgen.
10. Der Creator sieht im Creator-Dashboard, wie weit seine aktiven Sammelkäufe sind.

Beispiel:

Ein Creator erstellt ein Angebot für ein Drachenwürfel-Set. Die Produktion startet ab 20 Teilnehmern. Ab 40 Teilnehmern gibt es 10% Rabatt. Ab 60 Teilnehmern gibt es 20% Rabatt.

Ein Käufer tritt dem Angebot bei. Danach sieht er, dass nur noch wenige Teilnehmer bis zum Produktionsstart fehlen. Wenn mehr Personen teilnehmen, wird die nächste Rabattstufe freigeschaltet.

---

## Target Scope

Die erste Version von DealHive konzentriert sich bewusst auf einen kleinen, aber verständlichen Funktionsumfang.

Geplante Kernfunktionen:

- Login und Rollenauswahl
- Übersicht aktiver Sammelkäufe
- Detailseite eines Sammelkaufs
- Beitritt zu einem Sammelkauf
- Übersicht eigener Teilnahmen unter „Meine Hives“
- Creator-Dashboard
- Formular zum Erstellen eines neuen Sammelkaufs
- Anzeige von Mindestteilnehmern, Fortschritt und Rabattstufen

Nicht Teil des ersten Umfangs:

- echtes Bezahlsystem
- Versandabwicklung
- Chat-System
- Bewertungssystem
- automatische Rechnungen
- komplexe Lagerverwaltung

Diese Eingrenzung ist wichtig, damit das Projekt realistisch bleibt. DealHive soll zuerst zeigen, dass der zentrale Ablauf funktioniert: Creator erstellen Sammelkäufe, Käufer treten bei und beide Seiten können den Fortschritt nachvollziehen.

Die UI-Skizzen und Screen-Flows werden im Bereich [Solution Elements](product-discovery/03-solution-elements.md) dokumentiert.


## Ergänzung zum aktuellen App-Stand

Seit der ursprünglichen Formulierung der Value Proposition wurde der technische Umfang der App weiter konkretisiert. Die Grundidee bleibt gleich: DealHive soll Creator und Käufer bei Sammelkäufen im Bereich Brettspiele, TTRPGs, Tabletops und Zubehör zusammenbringen.

Der aktuelle App-Stand bildet den Kernprozess inzwischen konkreter ab:

* Creator können eigene Hives erstellen.
* Creator können eigene Hives im Creator Dashboard sehen.
* Creator können ihre eigenen Hives bearbeiten.
* Creator können Käufer eines Hives ansehen.
* Käufer können Hives entdecken und Detailseiten öffnen.
* Käufer können einem Hive mit einer bestimmten Menge beitreten.
* Käufer können ihre beigetretenen Hives unter „Meine Hives“ wiederfinden.
* Buyer und Creator können über einen einfachen Chat im Kontext eines Hives miteinander schreiben.
* Die App stellt über `/api/hives` eine einfache JSON-API bereit.

Damit wurde der Happy Path nicht nur konzeptionell beschrieben, sondern auch in der Flask-App umgesetzt. Besonders wichtig ist dabei, dass die App nicht als vollständiger Online-Shop gedacht ist. DealHive konzentriert sich weiterhin auf den ersten, realistischen MVP-Umfang: Sammelkäufe sichtbar machen, Nachfrage sammeln, Fortschritt zeigen und einfache Kommunikation zwischen Buyer und Creator ermöglichen.

Einige ursprünglich angedachte Felder aus den frühen Skizzen, zum Beispiel Material, Versandregion oder Produktbilder, sind im aktuellen MVP noch nicht vollständig umgesetzt. Stattdessen wurde der Umfang bewusst reduziert und auf die wichtigsten Felder beschränkt:

* Produktname
* Spielsystem
* Kurzbeschreibung
* Beschreibung
* Mindestmenge
* Basispreis
* Deadline
* Rabattstaffeln
