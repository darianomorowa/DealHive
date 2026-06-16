import sqlite3


def get_connection():
    # Datenbankdatei dealhive.db
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
            game_system TEXT NOT NULL,
            short_description TEXT NOT NULL,
            description TEXT NOT NULL,
            deadline TEXT NOT NULL,
            current_participants INTEGER NOT NULL,
            min_participants INTEGER NOT NULL
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL,
            street TEXT NOT NULL,
            postal_code TEXT NOT NULL,
            city TEXT NOT NULL,
            country TEXT NOT NULL
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS user_hives (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            hive_id INTEGER NOT NULL,
            relation_type TEXT NOT NULL,

            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (hive_id) REFERENCES hives(id),

            UNIQUE(user_id, hive_id, relation_type)
        )
    """)

    # commit fürs eigentliche Speichern
    connection.commit()
    connection.close()


# folgende Funktion wurde vollständig von KI generiert
def insert_test_hives(test_hives):
    connection = get_connection()

    # hier fügen wir Testdaten ein, die von außen übergeben werden
    # dadurch bleibt database.py übersichtlicher
    connection.executemany("""
        INSERT INTO hives (
            title,
            game_system,
            short_description,
            description,
            deadline,
            current_participants,
            min_participants
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, test_hives)

    # commit fürs eigentliche Speichern der Test-Hives
    connection.commit()
    connection.close()


def get_all_hives():
    connection = get_connection()

    # Daten aus der Tabelle abfragen
    hives = connection.execute("""
        SELECT id, 
        title, 
        game_system, 
        short_description, 
        deadline, 
        current_participants, 
        min_participants

        FROM hives
    """).fetchall()

    connection.close()
    return hives


def get_hive_by_id(hive_id):
    connection = get_connection()

    # hier suchen wir genau einen Hive über seine ID
    hive = connection.execute("""
        SELECT id, 
        title, 
        game_system, 
        short_description, 
        description, 
        deadline, 
        current_participants, 
        min_participants
        FROM hives
        WHERE id = ?
    """, (hive_id,)).fetchone()

    connection.close()

    # wir geben entweder den gefundenen Hive zurück oder "None",
    # falls nichts gefunden wurde
    return hive


def insert_hive(title, game_system, short_description, description, deadline, current_participants, min_participants):
    connection = get_connection()

    # hier speichern wir einen neuen Hive aus dem Creator-Formular
    connection.execute("""
        INSERT INTO hives (
            title,
            game_system,
            short_description,
            description,
            deadline,
            current_participants,
            min_participants
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        title,
        game_system,
        short_description,
        description,
        deadline,
        current_participants,
        min_participants
    ))

    # commit fürs eigentliche Speichern
    connection.commit()
    connection.close()


def create_test_user(username, name, email, password_hash, role, street, postal_code, city, country):
    connection = get_connection()

    # hier legen wir einen Testnutzer an, falls es ihn noch nicht gibt
    # INSERT OR IGNORE verhindert doppelte Testnutzer, wenn test_database.py mehrfach läuft
    connection.execute("""
        INSERT OR IGNORE INTO users (
            username,
            name,
            email,
            password_hash,
            role,
            street,
            postal_code,
            city,
            country
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        username,
        name,
        email,
        password_hash,
        role,
        street,
        postal_code,
        city,
        country
    ))

    # danach holen wir die ID, damit wir den Nutzer mit Hives verbinden können
    user = connection.execute("""
        SELECT id
        FROM users
        WHERE username = ?
    """, (username,)).fetchone()

    connection.commit()
    connection.close()

    return user["id"]


def assign_hive_to_user(user_id, hive_id, relation_type):
    connection = get_connection()

    # hier mappen wir einen User auf einen Hive
    # relation_type sagt, ob der Nutzer Creator oder Käufer dieses Hives ist
    connection.execute("""
        INSERT OR IGNORE INTO user_hives (
            user_id,
            hive_id,
            relation_type
        )
        VALUES (?, ?, ?)
    """, (
        user_id,
        hive_id,
        relation_type
    ))

    connection.commit()
    connection.close()


def get_hives_for_user(user_id, relation_type):
    connection = get_connection()

    # hier holen wir nur die Hives, die einer bestimmten user_id zugeordnet sind
    hives = connection.execute("""
        SELECT
            hives.id,
            hives.title,
            hives.game_system,
            hives.short_description,
            hives.deadline,
            hives.current_participants,
            hives.min_participants,
            user_hives.relation_type
        FROM hives
        JOIN user_hives ON hives.id = user_hives.hive_id
        WHERE user_hives.user_id = ?
        AND user_hives.relation_type = ?
    """, (
        user_id,
        relation_type
    )).fetchall()

    connection.close()

    return hives

def create_user_with_id(user_id, username, name, email, password_hash, role, street, postal_code, city, country):
    connection = get_connection()

    # hier legen wir einen Nutzer mit einer festen ID an
    # das nutzen wir aktuell für unseren Demo-Creator mit user_id 0
    connection.execute("""
        INSERT OR IGNORE INTO users (
            id,
            username,
            name,
            email,
            password_hash,
            role,
            street,
            postal_code,
            city,
            country
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        username,
        name,
        email,
        password_hash,
        role,
        street,
        postal_code,
        city,
        country
    ))

    connection.commit()
    connection.close()

    return user_id
def create_user(username, name, email, password_hash, role, street, postal_code, city, country):
    connection = get_connection()

    connection.execute("""
        INSERT INTO users (
            username,
            name,
            email,
            password_hash,
            role,
            street,
            postal_code,
            city,
            country
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        username,
        name,
        email,
        password_hash,
        role,
        street,
        postal_code,
        city,
        country
    ))

    connection.commit()
    connection.close()