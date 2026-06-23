---

{: .no_toc }

# 06: Flask-Routen nach Verantwortlichkeit aufteilen

## Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 23-Jun-2026

## Problemstellung

Am Anfang haben wir viele Flask-Routen direkt in `app.py` geschrieben. Für die ersten Schritte war das noch okay, weil man schnell sehen konnte, was passiert.

Bei DealHive wurde die Datei aber ziemlich schnell unübersichtlich. Es kamen immer mehr Bereiche dazu:

* Login, Registrierung und Profil
* Hive-Übersicht und Detailseiten
* Beitritt zu Hives
* Creator Dashboard
* Hive-Erstellung und Hive-Bearbeitung
* Chat und API

Dadurch wurde `app.py` immer unübersichtlicher. Man musste ständig scrollen, um die richtige Route zu finden. Noch schlimmer war aber das Merging: Wenn mehrere Leute gleichzeitig an derselben Datei arbeiten, wird das Konfliktmanagement beim Mergen sehr schnell sehr schlimm.

Auch die Aufgabenverteilung im Team wurde dadurch schwieriger. Wenn User-Logik, Creator-Logik und Hive-Logik alle in einer Datei liegen, ist nicht mehr sauber erkennbar, wer eigentlich an welchem Bereich arbeitet.

## Entscheidung

Wir haben entschieden, die Flask-Routen nach Verantwortlichkeit aufzuteilen.

Deshalb wurden besonders die User-Routes und Creator-Routes aus `app.py` ausgelagert. `app.py` bleibt dadurch eher der Startpunkt der Anwendung. Dort wird die App erstellt, die Datenbank initialisiert und die einzelnen Routenbereiche werden registriert.

Die eigentliche Fachlogik liegt in separaten Dateien:

```text
app.py
user_routes.py
hives.py
creator_routes.py
```

Dadurch ist klarer, wo welcher Teil der App liegt:

* `user_routes.py` kümmert sich um Registrierung, Login, Logout, Profil und Rollenwechsel
* `hives.py` kümmert sich um Hive-Übersicht, Detailseite, Beitritt, Chat und API
* `creator_routes.py` kümmert sich um Creator Dashboard, Hive-Erstellung und Hive-Bearbeitung
* `app.py` verbindet diese Teile miteinander und startet das Programm

Diese Struktur macht das Projekt leichter wartbar und die Teamarbeit etwas entspannter...

## Betrachtete Optionen

| Kriterium                   | Alles in `app.py`                            | Routen nach Bereichen aufteilen            | Sehr viele kleine Dateien                    |
| --------------------------- | -------------------------------------------- | ------------------------------------------ | -------------------------------------------- |
| **Übersichtlichkeit**       | Wurde schnell unübersichtlich                | Gut strukturiert                           | Kann zu kleinteilig werden                   |
| **Implementierungsaufwand** | Am Anfang niedrig                            | Mittel, aber gut machbar                   | Höher                                        |
| **Teamarbeit**              | Schwierig, weil alle dieselbe Datei anfassen | Besser, weil Bereiche getrennt sind        | Möglich, aber mehr Abstimmung nötig          |
| **Merging**                 | Konflikte wurden wahrscheinlicher            | Weniger Konflikte durch getrennte Bereiche | Weniger Konflikte, aber mehr Dateiverwaltung |
| **Wartbarkeit**             | Schwach bei wachsender App                   | Gut für unseren Umfang                     | Teilweise unnötig kompliziert                |
| **Prüfungserklärung**       | Schwerer, weil alles vermischt ist           | Gut am Projektaufbau zeigbar               | Könnte übertrieben wirken                    |

Wir haben uns für getrennte Routenmodule entschieden, weil wir ... nicht wirklich eine andere Wahl hatten...
