---

title: DD-09
parent: Design Decisions
nav_order: 9
------------

{: .no_toc }

# 09: Headless API für Hives bereitstellen

## Meta

Status
: **Work in progress**

Updated
: 23-Jun-2026

## Problemstellung

Eine technische Projektanforderung ist, dass die App mindestens eine Headless API bereitstellt. Das bedeutet, dass eine Route nicht einfach eine fertige HTML-Seite zurückgibt, sondern strukturierte Daten, zum Beispiel im JSON-Format.

DealHive ist sonst bewusst als klassische Flask- und Jinja-App gebaut. Die normalen Seiten werden serverseitig gerendert. Trotzdem soll die App zeigen, dass sie Daten auch unabhängig von HTML bereitstellen kann.

Die Frage war also, welche Daten sich für eine kleine API eignen, ohne direkt eine komplette REST-API mit Login, POST, PUT, DELETE und allem Drumherum bauen zu müssen.

## Entscheidung

Wir haben entschieden, zunächst eine kleine Headless API für Hives bereitzustellen.

Dafür gibt es die Route:

```text
/api/hives
```

Diese Route gibt öffentliche Hive-Daten als JSON zurück. Aktuell werden zum Beispiel Titel, Spielsystem, Kurzbeschreibung, Deadline, Mindestanzahl und aktuelle Teilnehmerzahl ausgegeben.

Die genaue Ausgestaltung der API ist aber noch offen. Die Route existiert bereits und erfüllt den Grundgedanken der Projektanforderung, aber wir wollen noch entscheiden, welche zusätzlichen Felder wirklich sinnvoll sind.

Mögliche Erweiterungen wären zum Beispiel:

* wie viele Teilnehmer oder Einheiten bis zur nächsten Rabattstufe fehlen
* welche Rabattstufe aktuell aktiv ist
* welcher Preis aktuell gilt
* ob das Mindestziel bereits erreicht wurde
* weitere Statusinformationen für externe Darstellungen

## Aktueller Stand

So sieht die API aktuell aus, wenn man `/api/hives` im Browser öffnet:

![Aktueller Stand der Headless API](../assets/images/Headless%20API%20Hives.JPG)

Wichtig ist: Die API ist keine zweite Datenbank. Die echten Daten liegen weiterhin in der SQLite-Datei. Die API liest nur ausgewählte Daten aus der Datenbank aus und stellt sie in einem anderen Format bereit.

Man kann sich das so vorstellen: SQLite ist der interne Lagerraum der App, während die API ein kleines Schaufenster nach außen ist. Nicht alles aus der Datenbank wird gezeigt, sondern nur das, was für diesen Datenzugriff sinnvoll ist.

Vereinfacht passiert dabei Folgendes:

```python
hives = get_all_hives()
return jsonify(hive_list)
```

Damit erfüllen wir die Projektanforderung einer Headless API, ohne DealHive künstlich zu einer großen API-Plattform umzubauen. Die App bleibt hauptsächlich eine serverseitig gerenderte Flask-App, hat aber zusätzlich einen kleinen API-Zugang für Hive-Daten.

## Bezug zu den Projektanforderungen

Diese Entscheidung unterstützt mehrere Anforderungen aus dem Projekt:

* Die App nutzt Flask als Webframework.
* Die Hauptseiten werden mit Jinja gerendert.
* Die Daten kommen aus der SQLite-Datenbank.
* Zusätzlich gibt es mindestens eine Route, die JSON statt HTML zurückgibt.
* Die API ist direkt im Browser oder mit Tools wie `curl` testbar.
* Die API bleibt klein genug, um zum aktuellen Projektumfang zu passen.

Dadurch zeigt DealHive nicht nur klassische Webseiten, sondern auch eine einfache technische Schnittstelle für Daten. Es ist also nicht nur Klicki-Klicki mit Templates, sondern hat auch einen kleinen API-Teil.

## Betrachtete Optionen

| Kriterium                   | Keine API                                       | Kleine Hive-API                     | Vollständige REST-API                   |
| --------------------------- | ----------------------------------------------- | ----------------------------------- | --------------------------------------- |
| **Projektanforderung**      | Würde die Anforderung nicht erfüllen            | Erfüllt die Grundanforderung        | Erfüllt sie auch, wäre aber zu groß     |
| **Implementierungsaufwand** | Niedrig                                         | Gut machbar                         | Hoch                                    |
| **Passung zu DealHive**     | Schwach, weil Hives nur als HTML sichtbar wären | Gut, weil Hives das Kernobjekt sind | Für unseren aktuellen Stand übertrieben |
| **Datenumfang**             | Keine JSON-Daten                                | Ausgewählte öffentliche Hive-Daten  | Sehr viele Daten und Methoden nötig     |
| **Weiterentwicklung**       | Keine Grundlage für externe Nutzung             | Gut erweiterbar                     | Mehr Architektur nötig                  |
| **Prüfungserklärung**       | Schwer zu verteidigen                           | Einfach am Code zeigbar             | Mehr Fragen zu REST, Auth und Methoden  |

Wir halten die konkrete Ausgestaltung der API bewusst offen. Der aktuelle Stand erfüllt die Projektanforderung und zeigt den technischen Ansatz. Welche zusätzlichen Felder später sinnvoll sind, zum Beispiel fehlende Teilnehmer bis zur nächsten Rabattstufe oder der aktuelle Preis, wird im weiteren Projektverlauf entschieden.
