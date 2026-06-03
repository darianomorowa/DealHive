from database import create_tables, get_connection


# hier starten wir erstmal nur die Funktion, die unsere Tabelle erstellt
create_tables()

# danach holen wir uns eine Verbindung zur Datenbank, um nachzuschauen
connection = get_connection()

# hier fragen wir SQLite, welche Tabellen es gerade gibt
tables = connection.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
""").fetchall() #Arbeitsspeicher concern... -> wenns laggt, dann deswegen

# wir geben die gefundenen Tabellen aus, damit wir sehen ob hives existiert
for table in tables:
    print(table["name"])
#"sqlite_sequence" kommt wegen AUTOINCREMENT - nicht hinterfragen...

# Verbindung wieder schließen, weil wir fertig sind
connection.close()

