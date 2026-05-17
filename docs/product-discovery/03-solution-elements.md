---
title: Solution Elements
parent: Product Discovery
nav_order: 3
---

{: .no_toc }
# Solution Elements

<details open markdown="block">
<summary>Table of contents</summary>
+ ToC
{: toc }
{: .text-delta }
</details>

## Workflow

Für diese Seite haben wir unsere bisherigen Projektideen und Entwürfe als Grundlage genutzt:

- den ursprünglichen Value Proposition Canvas
- die ersten UI-Skizzen
- die überarbeiteten v2-UI-Skizzen mit Domainbezug
- die Grundidee einer Sammelkaufplattform
- den neuen Fokus auf Brettspiele, TTRPGs, Tabletops und passendes Zubehör

Die ersten Skizzen waren noch allgemeiner gehalten. Sie haben uns geholfen, den groben Ablauf der App zu verstehen: anmelden, Angebote entdecken, ein Angebot im Detail ansehen, einem Sammelkauf beitreten und eigene Teilnahmen verwalten.

Danach wurden mehrere Screens als **v2** überarbeitet. Diese Versionen zeigen den Domainbezug deutlich stärker. Statt generischer Produkte stehen nun Beispiele wie Würfelsets, Dungeon-Terrain, Miniaturen, Würfeltürme, Spielmatten oder Token-Sets im Mittelpunkt.

---

## Grundidee der Anwendung

DealHive ist eine Web-App für Sammelkäufe im Bereich Brettspiele, TTRPGs, Tabletops und passendes Zubehör.

Creator, Künstler oder kleine Anbieter können Produkte als Sammelkauf anbieten. Käufer können diesen Angeboten beitreten. Wenn genug Personen teilnehmen, kann die Produktion starten. Bei größeren Gruppen können zusätzliche Rabattstufen freigeschaltet werden.

Der Kern der App bleibt bewusst überschaubar:

1. Ein Creator erstellt einen Sammelkauf.
2. Käufer entdecken das Angebot.
3. Käufer treten dem Sammelkauf bei.
4. Die App zeigt Fortschritt, Mindestziel und Rabattstufen.
5. Der Creator kann sehen, ob die Produktion möglich ist.

---

## Angepasster Value Proposition Canvas

### Käufer / Spieler

#### Aufgaben

Käufer möchten besondere Produkte für ihre Hobbys finden und sich an Sammelkäufen beteiligen, ohne selbst eine große Gruppe organisieren zu müssen.

Typische Aufgaben:

- interessante Produkte entdecken
- Produktdetails prüfen
- Preis und Rabattstufen verstehen
- einem Sammelkauf beitreten
- Fortschritt eines Angebots verfolgen
- sehen, wie viele Teilnehmer bis zur nächsten Rabattstufe fehlen

#### Gains

- besondere Produkte werden leichter auffindbar
- Gruppenrabatte können gemeinsam erreicht werden
- der Fortschritt eines Angebots ist sichtbar
- Sammelkäufe wirken strukturierter als in Chats oder Social Media
- Käufer müssen nicht selbst Leute zusammensuchen
- individuelle Produkte werden durch Mengenrabatte attraktiver

#### Pains

- handgemachte oder limitierte Produkte sind oft teuer
- interessante Angebote sind schwer zu finden
- Sammelbestellungen über Discord, Instagram oder WhatsApp sind schnell unübersichtlich
- Rabattschwellen sind allein kaum erreichbar
- es ist oft unklar, ob genug Leute mitmachen
- der aktuelle Stand einer Sammelbestellung ist nicht immer transparent

---

### Anbieter / Creator

#### Aufgaben

Anbieter möchten eigene Produkte sichtbar machen, Nachfrage prüfen und Sammelbestellungen einfacher organisieren.

Typische Aufgaben:

- Produktidee vorstellen
- Angebot erstellen
- Mindestmenge festlegen
- Rabattstufen definieren
- Teilnehmerzahl verfolgen
- Produktion erst starten, wenn genug Nachfrage da ist

#### Gains

- bessere Planung vor der Produktion
- weniger Risiko bei Kleinserien
- direkter Zugang zu Leuten aus der passenden Community
- sichtbare Teilnehmerzahlen
- weniger manuelle Koordination
- Rabattstufen können als Motivation genutzt werden

#### Pains

- Nachfrage ist vor der Produktion schwer einzuschätzen
- Materialkosten und Arbeitszeit entstehen oft früh
- kleine Produktionsmengen sind teuer
- manuelle Sammelbestellungen sind anstrengend zu verwalten
- Fortschritt muss sonst ständig selbst kommuniziert werden
- ohne zentrale Plattform ist es schwerer, genug interessierte Käufer zu erreichen

---

## Kernelemente der Anwendung

DealHive besteht aus mehreren einfachen Screens, die zusammen den wichtigsten Ablauf abbilden.

Die wichtigsten Bausteine sind:

- Login mit Rollenauswahl
- Sammelkäufe entdecken
- Sammelkauf im Detail ansehen
- Beitritt bestätigen
- Creator-Dashboard
- neuen Sammelkauf erstellen
- eigene Hives verwalten

Dabei geht es nicht darum, direkt einen kompletten Online-Shop zu bauen. Der Fokus liegt auf dem Sammelkauf-Prozess: Ein Creator stellt ein Angebot ein, Käufer treten bei, und die App zeigt transparent, wie weit der Hive bereits ist.

---

## Erklärung der Versionen

Für die UI-Skizzen verwenden wir zwei Arten von Versionen.

| Version | Bedeutung |
| :-- | :-- |
| ohne Versionsangabe | Erste Skizze. Diese Screens wurden bisher nicht überarbeitet oder waren für den aktuellen Stand ausreichend. |
| v1 | Erste Version eines Screens, bevor der Domainbezug stärker eingearbeitet wurde. |
| v2 | Überarbeitete Skizze mit stärkerem Domainbezug. Diese Screens enthalten konkrete Begriffe, Produkte und Abläufe aus der Brettspiel-, TTRPG- und Tabletop-Welt. |

Die v2-Screens sind die aktuelleren Screens und dienen für die weitere Entwicklung als Orientierung.

---

## Übersicht der UI-Skizzen

| Nr. | Screen | Datei | Version | Zweck | Änderung / Domainbezug |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | Login-Screen | [01-login-screen.jpeg](material/03-se/ui-screens/01-login-screen.jpeg) | ohne Versionsangabe | Einstieg in die App und Rollenauswahl | Dieser Screen wurde bisher nicht überarbeitet. Später könnte die Rollenauswahl noch klarer zwischen Käufer / Spieler und Creator / Anbieter unterscheiden. |
| 2 | Neue Anzeige erstellen | [02-neue-anzeige-erstellen-v1.jpeg](material/03-se/ui-screens/02-neue-anzeige-erstellen-v1.jpeg) | v1 | Erste Version des Formulars zum Erstellen eines Angebots | Diese Version zeigt den grundsätzlichen Ablauf, war aber noch allgemeiner gehalten. |
| 3 | Neue Anzeige erstellen | [02-neue-anzeige-erstellen-v2.jpeg](material/03-se/ui-screens/02-neue-anzeige-erstellen-v2.jpeg) | v2 | Formular zum Erstellen eines neuen Sammelkaufs | Die Skizze wurde deutlich domänenspezifischer. Das Formular enthält Felder wie Kategorie, Spielsystem, Material, Mindestteilnehmer, Basispreis und Rabattstufen. |
| 4 | Angebote entdecken | [03-angebote-entdecken-v1.jpeg](material/03-se/ui-screens/03-angebote-entdecken-v1.jpeg) | v1 | Erste Übersicht aktiver Angebote | Diese Version zeigte bereits die Grundidee einer Angebotsübersicht, war aber noch generischer. |
| 5 | Angebote entdecken | [03-angebote-entdecken-v2.png](material/03-se/ui-screens/03-angebote-entdecken-v2.png) | v2 | Übersicht aktiver Sammelkäufe | Die Skizze wurde auf Brettspiel-, TTRPG- und Tabletop-Produkte angepasst. Statt generischer Produkte werden Beispiele wie Würfelsets, Dungeon-Terrain, Miniaturen, Würfeltürme und Token-Sets gezeigt. |
| 6 | Anzeige im Detail | [04-anzeige-im-detail-v1.jpeg](material/03-se/ui-screens/04-anzeige-im-detail-v1.jpeg) | v1 | Erste Detailansicht eines Angebots | Diese Version zeigte den allgemeinen Aufbau einer Detailseite. |
| 7 | Anzeige im Detail | [04-anzeige-im-detail-v2.jpeg](material/03-se/ui-screens/04-anzeige-im-detail-v2.jpeg) | v2 | Detailansicht eines Sammelkaufs | Die Detailseite zeigt nun ein konkretes Beispiel wie ein Drachenwürfel-Set. Zusätzlich werden Creator, Spielsystem, Material, Versandregion, Teilnehmerstand und Rabattstufen angezeigt. |
| 8 | Beitritt bestätigen / Erfolgsseite | [05-beitritt-bestaetigen-erfolgsseite.jpeg](material/03-se/ui-screens/05-beitritt-bestaetigen-erfolgsseite.jpeg) | ohne Versionsangabe | Bestätigung des Beitritts zu einem Sammelkauf | Dieser Screen wurde bisher nicht überarbeitet. Inhaltlich passt er schon zum Ablauf, könnte aber später noch Begriffe wie Hive, Sammelkauf-Bedingungen oder konkrete Produktbeispiele enthalten. |
| 9 | Händler-Dashboard | [06-haendler-dashboard-v1.jpeg](material/03-se/ui-screens/06-haendler-dashboard-v1.jpeg) | v1 | Erste Übersicht für Anbieter | Diese Version war noch stärker an einem allgemeinen Händler-Dashboard orientiert. |
| 10 | Creator-Dashboard | [06-haendler-dashboard-v2.jpeg](material/03-se/ui-screens/06-haendler-dashboard-v2.jpeg) | v2 | Übersicht für Anbieter / Creator | Aus dem allgemeinen Händler-Dashboard wurde inhaltlich ein Creator-Dashboard. Die Beispielangebote beziehen sich nun auf Produkte wie Drachenwürfel-Sets, Dungeon-Terrain, Holz-Würfeltürme und Miniaturen. |
| 11 | Meine Einkaufsgruppen | [07-meine-einkaufsgruppen-v1.jpeg](material/03-se/ui-screens/07-meine-einkaufsgruppen-v1.jpeg) | v1 | Erste Übersicht der eigenen Teilnahmen | Diese Version zeigte bereits die Idee, dass Käufer ihre Gruppen verfolgen können. |
| 12 | Meine Hives | [07-meine-hives-v2.jpeg](material/03-se/ui-screens/07-meine-hives-v2.jpeg) | v2 | Übersicht der Sammelkäufe, denen ein Käufer beigetreten ist | Aus „Meine Einkaufsgruppen“ wurde „Meine Hives“. Der Begriff „Hive“ ist eine app-spezifische Bezeichnung für einen Sammelkauf und passt zum Namen DealHive. |

---

## UI-Skizzen im Detail

### 1. Login-Screen

![Login-Screen](material/03-se/ui-screens/01-login-screen.jpeg)

Der Login-Screen ist der Einstieg in die Anwendung. Nutzer können sich anmelden und später je nach Rolle unterschiedliche Funktionen nutzen.

Für die weitere Entwicklung ist wichtig, dass die Rollen klar erkennbar sind. Käufer sollen Angebote entdecken und beitreten können. Creator sollen eigene Sammelkäufe erstellen und verwalten können.

---

### 2. Neue Anzeige erstellen v1

![Neue Anzeige erstellen v1](material/03-se/ui-screens/02-neue-anzeige-erstellen-v1.jpeg)

Diese erste Version zeigt das Grundprinzip für das Erstellen eines Angebots. Der Screen war noch allgemeiner gehalten und diente vor allem dazu, die Struktur des Formulars zu planen.

---

### 3. Neue Anzeige erstellen v2

![Neue Anzeige erstellen v2](material/03-se/ui-screens/02-neue-anzeige-erstellen-v2.jpeg)

Dieser Screen zeigt, wie ein Creator einen neuen Sammelkauf erstellt.

Die v2-Version ist deutlich stärker auf den Domainbezug angepasst. Das Formular enthält Felder, die für Brettspiel-, TTRPG- und Tabletop-Produkte sinnvoll sind:

- Produktname
- Kategorie
- Spielsystem
- Material
- Beschreibung
- Produktbild
- Mindestteilnehmer
- Basispreis
- Rabattstufen
- Deadline
- Versandregion

Dadurch kann ein Creator nicht nur irgendein Produkt einstellen, sondern ein Angebot mit passenden Informationen für die Hobby-Community erstellen.

---

### 4. Angebote entdecken v1

![Angebote entdecken v1](material/03-se/ui-screens/03-angebote-entdecken-v1.jpeg)

Diese erste Version zeigt die Grundstruktur der Angebotsübersicht. Sie war hilfreich, um zu verstehen, wie Nutzer Angebote finden und vergleichen können.

---

### 5. Angebote entdecken v2

![Angebote entdecken v2](material/03-se/ui-screens/03-angebote-entdecken-v2.png)

Die überarbeitete Angebotsübersicht zeigt aktive Sammelkäufe aus der Brettspiel-, TTRPG- und Tabletop-Welt.

Der Domainbezug wird hier vor allem durch die Produktbeispiele sichtbar. Statt allgemeiner Produkte stehen nun konkrete Hobbyprodukte im Vordergrund, zum Beispiel:

- Drachenwürfel-Set
- Dungeon-Terrain-Set
- Holz-Würfelturm
- Goblin-Miniaturen-Set
- Kampagnen-Token-Set
- Resin-Würfel

Zusätzlich wurden Such- und Filterbegriffe angepasst. Nutzer können nach Würfeln, Terrain, Miniaturen oder Zubehör suchen. Dadurch wirkt der Screen nicht mehr wie ein beliebiger Marktplatz, sondern wie eine Plattform für eine konkrete Community.

---

### 6. Anzeige im Detail v1

![Anzeige im Detail v1](material/03-se/ui-screens/04-anzeige-im-detail-v1.jpeg)

Diese erste Version zeigt den grundsätzlichen Aufbau einer Detailseite. Nutzer können dort Informationen zu einem Angebot sehen und dem Angebot beitreten.

---

### 7. Anzeige im Detail v2

![Anzeige im Detail v2](material/03-se/ui-screens/04-anzeige-im-detail-v2.jpeg)

Die Detailseite zeigt alle wichtigen Informationen zu einem einzelnen Sammelkauf.

Im Beispiel geht es um ein Drachenwürfel-Set. Dadurch wird der Domainbezug direkt sichtbar. Neben Preis und Beschreibung werden auch Informationen angezeigt, die für diese Art von Produkt wichtig sind:

- Kategorie
- Spielsystem
- Creator
- Material
- Versandregion
- Teilnehmerstand
- Rabattstufen

Besonders wichtig ist die Fortschrittsanzeige. Käufer sehen, wie viele Personen bereits teilnehmen und wie viele noch bis zum Produktionsstart fehlen.

---

### 8. Beitritt bestätigen / Erfolgsseite

![Beitritt bestätigen / Erfolgsseite](material/03-se/ui-screens/05-beitritt-bestaetigen-erfolgsseite.jpeg)

Dieser Screen zeigt den Moment, in dem ein Käufer einem Sammelkauf beitritt.

Der Screen wurde bisher nicht als v2 überarbeitet, passt aber grundsätzlich schon zum Ablauf der App. Vor dem Beitritt sollen Nutzer noch einmal sehen, welchem Angebot sie beitreten und welche Bedingungen gelten.

Für eine spätere Version könnte der Screen noch stärker auf DealHive angepasst werden, zum Beispiel durch Begriffe wie „Hive“, „Sammelkauf-Bedingungen“ oder konkrete Produktbeispiele.

---

### 9. Händler-Dashboard v1

![Händler-Dashboard v1](material/03-se/ui-screens/06-haendler-dashboard-v1.jpeg)

Diese erste Version war noch stärker an einem allgemeinen Händler-Dashboard orientiert. Sie zeigt aber bereits die Idee, dass Anbieter ihre eigenen Angebote verwalten können.

---

### 10. Creator-Dashboard v2

![Creator-Dashboard v2](material/03-se/ui-screens/06-haendler-dashboard-v2.jpeg)

Dieser Screen wurde von einem allgemeinen Händler-Dashboard zu einem Creator-Dashboard weiterentwickelt.

Der Begriff „Creator“ passt besser zur Domäne, weil viele Anbieter in der Brettspiel- und TTRPG-Community keine klassischen Händler sind. Es können auch Künstler, Handwerker, Miniaturenbemaler, Terrainbauer oder Würfelmacher sein.

Das Dashboard zeigt:

- aktive Sammelkäufe
- Teilnehmer insgesamt
- erfolgreiche Produktionen
- eigene Angebote
- letzte Aktivitäten
- Schnellaktionen

Die Beispielangebote wurden ebenfalls an den Domainbezug angepasst, zum Beispiel Drachenwürfel-Sets, Dungeon-Terrain und Holz-Würfeltürme.

---

### 11. Meine Einkaufsgruppen v1

![Meine Einkaufsgruppen v1](material/03-se/ui-screens/07-meine-einkaufsgruppen-v1.jpeg)

Diese erste Version zeigt, dass Käufer ihre eigenen Teilnahmen an Gruppenkäufen verfolgen können. Der Screen war funktional, aber noch allgemeiner formuliert.

---

### 12. Meine Hives v2

![Meine Hives v2](material/03-se/ui-screens/07-meine-hives-v2.jpeg)

Dieser Screen zeigt alle Sammelkäufe, denen ein Käufer beigetreten ist.

Aus „Meine Einkaufsgruppen“ wurde „Meine Hives“. Der Begriff „Hive“ ist eine app-spezifische Bezeichnung für einen Sammelkauf. Dadurch passt die Sprache der App besser zum Namen DealHive.

Damit der Begriff verständlich bleibt, wird im Screen erklärt, dass es sich um Sammelkäufe handelt, bei denen der Nutzer mitmacht.

Die Seite zeigt:

- aktive Hives
- erreichte Ziele
- abgeschlossene Hives
- eigene Teilnahmen
- nächste Schritte
- Fortschritt einzelner Angebote

---

## Wichtigste Änderungen durch den Domainbezug

Die v2-Skizzen wurden nicht komplett neu gedacht, sondern gezielt an den Domainbezug angepasst.

Der grundlegende Ablauf der App bleibt gleich:

1. Nutzer melden sich an.
2. Creator erstellen Sammelkauf-Angebote.
3. Käufer entdecken Angebote.
4. Käufer öffnen eine Detailseite.
5. Käufer treten einem Sammelkauf bei.
6. Creator verwalten ihre Angebote.
7. Käufer verfolgen ihre eigenen Teilnahmen.

Die wichtigsten Änderungen sind:

- Aus allgemeinen Anzeigen wurden Sammelkäufe.
- Aus Händlern wurden Creator / Anbieter.
- Aus Einkaufsgruppen wurden Hives.
- Produktbeispiele wurden auf die Domäne angepasst.
- Die Screens zeigen nun Würfelsets, Miniaturen, Dungeon-Terrain, Würfeltürme, Spielmatten und Token-Sets.
- Die Formulare enthalten domänenspezifische Felder wie Spielsystem und Material.
- Die Fortschrittsanzeigen beziehen sich auf Produktionsstart und Rabattstufen.
- Der Domainbezug ist nicht nur in der Beschreibung sichtbar, sondern direkt in der Oberfläche.