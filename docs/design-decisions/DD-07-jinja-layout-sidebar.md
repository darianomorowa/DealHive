---

title: DD-07
parent: Design Decisions
nav_order: 7
------------

{: .no_toc }

# 07: Gemeinsames Jinja-Layout und Sidebar für die Navigation nutzen

## Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 23-Jun-2026

## Problemstellung

DealHive besteht aus mehreren Seiten: Login, Registrierung, Hive-Übersicht, Detailseiten, Creator Dashboard, Profil, Chat und weitere Bereiche. Damit Nutzer sich in der App zurechtfinden, brauchten wir eine einheitliche Navigation.

Am Anfang hätten wir die Navigation theoretisch in jede HTML-Datei einzeln schreiben können. Das wäre aber schnell nervig und fehleranfällig geworden. Wenn man dann später einen Link ändern möchte, müsste man ihn an mehreren Stellen anfassen. Natürlich würde man dabei garantiert irgendeine Datei vergessen, weil HTML-Dateien manchmal wie kleine Goblins im Projektordner leben.

Außerdem kannten wir aus OOP2 schon das Grundprinzip, dass man gemeinsame Struktur nicht ständig kopieren sollte. Es ist hier zwar keine Vererbung mit Klassen wie in Java oder Python, aber Jinja bietet mit `extends` und `block` ein ähnliches Prinzip für Templates.

## Entscheidung

Wir haben entschieden, ein gemeinsames Jinja-Layout zu verwenden.

Die Datei `layout.html` dient als Grundgerüst für die Seiten. Andere Templates können dieses Layout verwenden und nur den eigenen Inhalt austauschen. Dadurch müssen allgemeine Bestandteile wie Seitenstruktur, Styles und Navigation nicht überall neu geschrieben werden.

Zusätzlich gibt es eine gemeinsame Sidebar als Partial:

```text
templates/layout.html
templates/partials/sidebar.html
```

Die Sidebar hilft bei der Navigation durch die App. Sie zeigt wichtige Bereiche wie Hives, Profil, Creator Dashboard oder Login abhängig davon, ob ein Nutzer angemeldet ist und welche Rolle aktiv ist.

Dadurch bleibt die App einheitlicher. Neue Seiten fühlen sich nicht wie komplett fremde Screens an, sondern passen zum restlichen Aufbau.

## Betrachtete Optionen

| Kriterium                   | Navigation in jeder Datei einzeln            | Gemeinsames Layout mit Sidebar            | Komplett eigenes Layout pro Bereich |
| --------------------------- | -------------------------------------------- | ----------------------------------------- | ----------------------------------- |
| **Übersichtlichkeit**       | Wird schnell unübersichtlich                 | Gut strukturiert                          | Uneinheitlich                       |
| **Wartbarkeit**             | Schwach, weil Änderungen mehrfach nötig sind | Gut, weil zentrale Stellen genutzt werden | Mittel, aber unnötig aufwendig      |
| **Design-Konsistenz**       | Schwer zu halten                             | Einheitliches Erscheinungsbild            | Risiko für unterschiedliche Designs |
| **Implementierungsaufwand** | Am Anfang niedrig, später nervig             | Gut machbar                               | Höher                               |
| **Navigation**              | Links müssten mehrfach gepflegt werden       | Sidebar bündelt wichtige Links            | Nutzerführung weniger klar          |
| **Prüfungserklärung**       | Weniger sauber erklärbar                     | Gut am Template-Aufbau zeigbar            | Könnte übertrieben wirken           |

Wir haben uns für ein gemeinsames Jinja-Layout mit Sidebar entschieden, weil die App dadurch einheitlicher, wartbarer und leichter navigierbar bleibt. Gleichzeitig konnten wir ein Prinzip wiederverwenden, das wir aus OOP2 kannten: gemeinsame Struktur einmal definieren und danach an mehreren Stellen nutzen.
