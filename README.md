<p align="center">
  <img src="docs/assets/images/dealhive-logo.png" alt="DealHive Logo" style="max-width: 100%; height: auto;">
</p>

# DealHive

DealHive ist eine Flask-Web-App für Sammelkäufe im Bereich Brettspiele, TTRPGs, Tabletops und Zubehör.

Creator, Künstler, Handwerker oder kleine Anbieter können limitierte Produkte als Sammelkauf anbieten. Käufer können diesen Angeboten beitreten. Sobald genügend Personen teilnehmen, kann die Produktion starten. Bei größeren Gruppen können Rabattstufen freigeschaltet werden, zum Beispiel 10% oder 20%.

## Kernidee

Ein Creator erstellt einen Hive, zum Beispiel für ein handgemachtes Würfelset.

Beispiel:

* Produktion ab 20 Teilnehmern
* 10% Rabatt ab 40 Teilnehmern
* 20% Rabatt ab 60 Teilnehmern

Käufer können dem Hive beitreten, eine Menge auswählen, den Fortschritt verfolgen und mit dem Creator schreiben.

## Team

* [Darian Omorowa](https://github.com/darianomorowa)
* [Daniil Ioffe](https://github.com/gittyDanny)
* [Haya Al-Abbasi](https://github.com/HayaHWR)
* [Matthieu Weinlein](https://github.com/mttwln)

## Dokumentation

Die Projektdokumentation ist hier auffindbar:

https://darianomorowa.github.io/DealHive/#dealhive

## Technischer Überblick

Die App verwendet:

* Python
* Flask
* Jinja2 Templates
* SQLite
* HTML und CSS

Wichtige Dateien:

| Datei / Ordner      | Zweck                                                                    |
| :------------------ | :----------------------------------------------------------------------- |
| `app.py`            | Startpunkt der Flask-App und Registrierung der Routenmodule              |
| `database.py`       | SQLite-Verbindung, Tabellen und Datenbankfunktionen                      |
| `hives.py`          | Hive-Übersicht, Hive-Detailseite, Beitritt, Chat und JSON-API            |
| `creator_routes.py` | Creator Dashboard, Hive-Erstellung, Hive-Bearbeitung und Käuferübersicht |
| `user_routes.py`    | Registrierung, Login, Profil, Rollenwechsel und Meine Hives              |
| `templates/`        | Jinja2-Templates für die HTML-Seiten                                     |
| `docs/`             | Projektdokumentation und GitHub-Pages-Inhalte                            |
| `dealhive.db`       | SQLite-Datenbankdatei für die lokale Ausführung                          |
| `test_database.py`  | Skript zum Erzeugen reproduzierbarer Testdaten                           |

## App lokal starten

Diese Anleitung beschreibt den kompletten lokalen Start nach dem Klonen des Repositories.

### 1. Repository klonen

```bash
git clone https://github.com/darianomorowa/DealHive.git
cd DealHive
```

Falls das Repository bereits lokal vorhanden ist:

```bash
git pull origin main
```

### 2. Virtuelle Umgebung erstellen

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Abhängigkeiten installieren

Windows:

```powershell
python -m pip install -r requirements.txt
```

macOS / Linux:

```bash
python3 -m pip install -r requirements.txt
```

### 4. Datenbank und Testdaten

Für die First Submission enthält das Repository eine SQLite-Datenbankdatei:

```text
dealhive.db
```

Diese Datei ist die mitgelieferte Demo-Datenbank für die lokale Ausführung der App. Dadurch kann die App nach dem Klonen direkt mit vorhandenen Testdaten ausprobiert werden.

Zusätzlich gibt es die Datei:

```text
test_database.py
```

Diese Datei ist bewusst als Skript zur Erzeugung von Testdaten gedacht.

Der Hintergrund ist: Während der lokalen Entwicklung entstehen durch Registrierung, Hive-Erstellung, Beitritte und Chats viele Testdaten. Diese lokalen Experimente sollen nicht unkontrolliert die Demo-Datenbank verschmutzen, die für die Bewertung nachvollziehbar bleiben soll.

Deshalb gilt:

* `dealhive.db` ist die mitgelieferte Demo-Datenbank für die First Submission.
* `test_database.py` kann verwendet werden, um bei Bedarf eine neue lokale Testdatenbank mit Grunddaten zu erzeugen.
* Lokale Experimente sollten nicht automatisch als neue Bewertungsdatenbank committed werden.

Falls die mitgelieferte Datenbank fehlt oder lokal neu aufgebaut werden soll, sollte zuerst die alte lokale Datenbank umbenannt oder gelöscht werden. Danach kann `test_database.py` ausgeführt werden.

Windows PowerShell:

```powershell
Rename-Item dealhive.db dealhive_alt.db
python test_database.py
```

macOS / Linux:

```bash
mv dealhive.db dealhive_alt.db
python3 test_database.py
```

Falls noch keine Datenbankdatei vorhanden ist, reicht direkt:

Windows:

```powershell
python test_database.py
```

macOS / Linux:

```bash
python3 test_database.py
```

### 5. Flask-App starten

Windows:

```powershell
python app.py
```

macOS / Linux:

```bash
python3 app.py
```

Danach im Browser öffnen:

```text
http://127.0.0.1:5001/
```

Die App läuft standardmäßig auf Port `5001`.

## Demo-Zugänge

Nach Ausführung von `test_database.py` sind folgende Creator-Testnutzer vorhanden:

| Rolle   | Username            | Passwort  |
| :------ | :------------------ | :-------- |
| Creator | `dice_creator`      | `test123` |
| Creator | `terrain_creator`   | `test123` |
| Creator | `miniature_creator` | `test123` |

Zusätzlich kann jederzeit ein neuer Nutzer über die Registrierungsseite angelegt werden.

Für den Buyer-Flow empfiehlt es sich, direkt über die App einen neuen Buyer zu registrieren.

## Happy Path für Prüfer

Der folgende Ablauf zeigt die wichtigsten Funktionen der App.

### Happy Path 1: Als Creator einen Hive erstellen

1. App starten.
2. Im Browser `http://127.0.0.1:5001/` öffnen.
3. Auf `Registrieren` klicken.
4. Einen neuen Nutzer mit Rolle `creator` anlegen.
5. Einloggen.
6. In der Sidebar auf `Hive erstellen` klicken.
7. Einen neuen Hive anlegen.

Beispieldaten:

| Feld              | Beispiel                                        |
| :---------------- | :---------------------------------------------- |
| Titel             | `Demo Würfelset`                                |
| Spielsystem       | `Systemunabhängig`                              |
| Kurzbeschreibung  | `Handgemachtes Würfelset für TTRPGs`            |
| Beschreibung      | `Ein kleines Demo-Angebot für einen Sammelkauf` |
| Mindestteilnehmer | `5`                                             |
| Basispreis        | `20`                                            |
| Deadline          | `30.06.2026`                                    |

Optionale Rabattstaffeln:

| Mindestmenge | Rabatt |
| :----------- | :----- |
| `10`         | `10`   |
| `20`         | `20`   |

Danach:

1. Hive speichern.
2. Im Creator Dashboard prüfen, ob der Hive angezeigt wird.
3. Über `Hive bearbeiten` die Daten oder Rabattstaffeln anpassen.
4. Über `Käufer ansehen` die Käuferübersicht öffnen.

### Happy Path 2: Als Buyer einem Hive beitreten

1. Ausloggen oder einen zweiten Browser / privaten Tab verwenden.
2. Auf `Registrieren` klicken.
3. Einen neuen Nutzer mit Rolle `buyer` anlegen.
4. Einloggen.
5. In der Sidebar auf `Hives ansehen` klicken.
6. Einen Hive öffnen.
7. Eine Menge auswählen.
8. Dem Hive beitreten.
9. In der Sidebar auf `Meine Hives` klicken.
10. Prüfen, ob der beigetretene Hive angezeigt wird.

### Happy Path 3: Chat zwischen Buyer und Creator

1. Als Buyer einen Hive öffnen.
2. Auf der Detailseite den Chat mit dem Creator öffnen.
3. Eine Nachricht schreiben.
4. Als Creator einloggen.
5. In der Sidebar auf `Meine Chats` oder im Creator-Bereich auf die Käuferübersicht gehen.
6. Den Chat öffnen und die Nachricht prüfen.

### Happy Path 4: Headless API prüfen

Die App stellt eine JSON-API bereit:

```text
http://127.0.0.1:5001/api/hives
```

Diese Route gibt die vorhandenen Hives als JSON zurück.

## Wichtige Routen

| Route                           | Bedeutung                     |
| :------------------------------ | :---------------------------- |
| `/`                             | Startseite                    |
| `/register`                     | Registrierung                 |
| `/login`                        | Login                         |
| `/profile`                      | Profil                        |
| `/profile/edit`                 | Profil bearbeiten             |
| `/hives`                        | Hive-Übersicht                |
| `/hives/<id>`                   | Detailseite eines Hives       |
| `/hives/<id>/join`              | Beitritt zu einem Hive        |
| `/hives/<id>/chat/<partner_id>` | Privater Chat zu einem Hive   |
| `/my-hives`                     | Hives des eingeloggten Buyers |
| `/my-chats`                     | Chatübersicht                 |
| `/creator/dashboard`            | Creator Dashboard             |
| `/creator/hives/new`            | Neuen Hive erstellen          |
| `/creator/hives/<id>/edit`      | Hive bearbeiten               |
| `/creator/hives/<id>/buyers`    | Käuferübersicht für Creator   |
| `/api/hives`                    | JSON-API mit Hive-Daten       |

## Anforderungen der First Submission

Diese App erfüllt die zentralen technischen Anforderungen der First Submission:

| Anforderung               | Umsetzung in DealHive                                                                   |
| :------------------------ | :-------------------------------------------------------------------------------------- |
| Python                    | App ist in Python geschrieben                                                           |
| Flask                     | Flask wird als Webframework verwendet                                                   |
| Jinja2                    | Templates liegen im Ordner `templates/` und verwenden Jinja2                            |
| Mehrere HTTP-Routen       | App hat getrennte Routen für Registrierung, Login, Hives, Creator-Bereich, Chat und API |
| SQLite                    | App verwendet `dealhive.db` als SQLite-Datenbank                                        |
| Genau eine Datenbankdatei | `dealhive.db` ist die lokale SQLite-Datenbank                                           |
| User-Rollen               | Es gibt `buyer` und `creator`                                                           |
| Autorisierung             | Creator-Bereiche prüfen Login, Rolle und teilweise Ownership                            |
| Headless API              | `/api/hives` liefert JSON                                                               |
| Kein JavaScript           | Die App nutzt HTML, CSS, Flask und Jinja2, aber kein eigenes JavaScript                 |
| Lokal ausführbar          | Start über `python app.py` oder `python3 app.py`                                        |

## Hinweise zur lokalen Ausführung

* Die App läuft auf `http://127.0.0.1:5001/`.
* Die Datenbankdatei heißt `dealhive.db`.
* Wenn eine alte lokale Datenbank Probleme macht, sollte sie umbenannt und mit `test_database.py` neu erzeugt werden.
* Falls sich Datenbankstruktur und lokale Datenbank unterscheiden, kann eine alte `dealhive.db` Fehler verursachen.
* In diesem Fall sollte die lokale Datei umbenannt werden, damit die Tabellen neu erzeugt werden können.
* Es wird kein Docker, keine VM und keine externe Datenbank verwendet.
* Es wird kein eigenes JavaScript verwendet.

## Kurzer Test vor Abgabe

Vor der Abgabe kann lokal geprüft werden:

Windows:

```powershell
python -m py_compile app.py database.py hives.py creator_routes.py user_routes.py pricing_logic.py
python app.py
```

macOS / Linux:

```bash
python3 -m py_compile app.py database.py hives.py creator_routes.py user_routes.py pricing_logic.py
python3 app.py
```

Danach im Browser prüfen:

```text
http://127.0.0.1:5001/
http://127.0.0.1:5001/hives
http://127.0.0.1:5001/api/hives
```
