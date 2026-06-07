<p align="center">
  <img src="docs/assets/images/dealhive-logo.png" alt="DealHive Logo" style="max-width: 100%; height: auto;">
</p>

# DealHive

DealHive ist eine Web-App für Sammelkäufe im Bereich Brettspiele, TTRPGs, Tabletops und Zubehör.

Creator, Künstler, Handwerker oder kleine Anbieter können limitierte Produkte als Sammelkauf anbieten. Käufer können diesen Angeboten beitreten. Sobald genügend Personen teilnehmen, kann die Produktion starten. Bei größeren Gruppen können Rabattstufen freigeschaltet werden, zum Beispiel 10% oder 20%.

## Kernidee

Ein Creator erstellt einen Hive, zum Beispiel für ein handgemachtes Würfelset.

Beispiel:

- Produktion ab 20 Teilnehmern
- 10% Rabatt ab 40 Teilnehmern
- 20% Rabatt ab 60 Teilnehmern

Käufer können dem Hive beitreten und den Fortschritt verfolgen.

## Dokumentation

Die Projektdokumentation ist hier auffindbar:

https://darianomorowa.github.io/DealHive/#dealhive

## App Setup

_Folgt mit First Submission_

## Team

- [Darian Omorowa](https://github.com/darianomorowa)
- [Daniil Ioffe](https://github.com/gittyDanny)
- [Haya Al-Abbasi](https://github.com/HayaHWR)
- [Matthieu Weinlein](https://github.com/mttwln)

## App Setup (Lokaler Start)

Folge diesen Schritten, um die DealHive-App lokal auf deinem Computer zu starten:

1. **Repository klonen / Projektordner öffnen:**
   Stelle sicher, dass du dich im Hauptverzeichnis `DealHive` befindest und dein Terminal dort geöffnet ist.

2. **Abhängigkeiten installieren:**
   Installiere die benötigten Pakete (wie Flask) über die `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. **Datenbank vorbereiten:**
   Die App erstellt beim ersten Start automatisch die SQLite-Datenbank `dealhive.db` und die benötigten Tabellen im Hintergrund.

4. **Server starten:**
   Starte den Flask-Server mit folgendem Befehl im Terminal:
   ```bash
   python3 app.py
   ```
5. **App im Browser aufrufen:**
   Öffne deinen Browser und gehe auf:
   * Hauptseite: `http://127.0.0.1:5001/`
   * Hive erstellen: `http://127.0.0.1:5001/creator/hives/new`