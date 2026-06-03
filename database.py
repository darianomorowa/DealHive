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