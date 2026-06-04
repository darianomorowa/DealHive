import sqlite3


def get_connection():
    #Datenbankdatei dealhive.db
    connection = sqlite3.connect("dealhive.db")
    # dadurch können wir später auf Spaltennamen zugreifen z.B. hive["title"]
    connection.row_factory = sqlite3.Row
    # wir geben die Verbindung zurück, damit andere Funktionen sie nutzen können
    return connection


def create_tables():
     # hier holen wir uns eine Verbindung zur Datenbank
    connection = get_connection()
    # AUTOINCREMENT ist insane - es generiert selber IDs!!!
    # (jede Zeile bekommt eine eigene ID)
    # rest ist stanbdart DDL oder so
    connection.execute("""
        CREATE TABLE IF NOT EXISTS hives (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            deadline TEXT NOT NULL,
            current_participants INTEGER NOT NULL,
            min_participants INTEGER NOT NULL
        )
    """)
    # commit fürs eigentliche Speichern
    connection.commit()
    connection.close()

#folgende Funktion wurde vollständig von KI generiert
def insert_test_hives():
    connection = get_connection()

    # hier legen wir 10 Test-Hives an, damit die Übersicht nicht leer ist
    # Reihenfolge ist wichtig: title, deadline, current_participants, min_participants
    test_hives = [
        ("Drachenwürfel-Set", "31.05.2026", 18, 20),
        ("Dungeon-Terrain-Set", "28.05.2026", 31, 40),
        ("Holz-Würfelturm", "02.06.2026", 12, 25),
        ("Goblin-Miniaturen-Set", "05.06.2026", 22, 30),
        ("Zauberbuch-Kartenhalter", "10.06.2026", 9, 15),
        ("Kampagnen-Token-Set", "15.06.2026", 44, 50),
        ("Resin-Würfel Nebelblau", "20.06.2026", 7, 20),
        ("Tabletop-Spielmatte", "25.06.2026", 16, 30),
        ("Mimic-Würfelturm", "30.06.2026", 11, 25),
        ("Abenteuer-Modul: Krypta der Bienenkönigin", "05.07.2026", 14, 20),
    ]

    # executemany ist wie INSERT in Schleife, nur sauberer
    # jeder Tupel aus test_hives wird einmal in die Tabelle geschrieben
    connection.executemany("""
        INSERT INTO hives (
            title,
            deadline,
            current_participants,
            min_participants
        )
        VALUES (?, ?, ?, ?)
    """, test_hives)

    # commit fürs eigentliche Speichern der 10 Test-Hives
    connection.commit()
    connection.close()


def get_all_hives():
    connection = get_connection()

    # Daten aus der Tabelle abfragen
    hives = connection.execute("""
        SELECT id, title, deadline, current_participants, min_participants
        FROM hives
    """).fetchall()

    connection.close()
    return hives

def get_hive_by_id(hive_id):
    connection = get_connection()

    # hier suchen wir genau einen Hive über seine ID
    hive = connection.execute("""
        SELECT id, title, deadline, current_participants, min_participants
        FROM hives
        WHERE id = ?
    """, (hive_id,)).fetchone()

    connection.close()

    # wir geben entweder den gefundenen Hive zurück oder "None",
    # falls nichts gefunden wurde
    return hive