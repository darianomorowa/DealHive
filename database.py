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
            title TEXT NOT NULL
            
        )
    """)
    # commit fürs eigentliche Speichern
    connection.commit()
    connection.close()

def insert_test_hive():
    connection = get_connection()

    # hier fügen wir erstmal einen Test-Hive ein
    # AUTOINCREMENT macht selber neue ID
    connection.execute("""
        INSERT INTO hives (title)
        VALUES (?)
    """, ("Drachenwürfel-Set",))

    connection.commit()
    connection.close()


def get_all_hives():
    connection = get_connection()

    # Daten aus der Tabelle abfragen
    hives = connection.execute("""
        SELECT id, title
        FROM hives
    """).fetchall()

    connection.close()
    return hives

def get_hive_by_id(hive_id):
    connection = get_connection()

    # hier suchen wir genau einen Hive über seine ID
    hive = connection.execute("""
        SELECT id, title
        FROM hives
        WHERE id = ?
    """, (hive_id,)).fetchone()

    connection.close()

    # wir geben entweder den gefundenen Hive zurück oder "None",
    # falls nichts gefunden wurde
    return hive