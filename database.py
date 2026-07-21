import sqlite3
from contextlib import contextmanager
from datetime import date
from pathlib import Path


# dadurch wird immer die Datenbank neben dieser Python-Datei verwendet
DATABASE_PATH = Path(__file__).resolve().parent / "dealhive.db"

def parse_deadline(deadline_value):
    try:
        return date.fromisoformat(deadline_value)
    except (TypeError, ValueError):
        return None


def is_deadline_expired(deadline_value):
    parsed_deadline = parse_deadline(deadline_value)

    # Ungültige Daten werden sicherheitshalber als abgelaufen behandelt.
    if parsed_deadline is None:
        return True

    return parsed_deadline < date.today()


def get_hive_status(
    deadline_value,
    current_quantity,
    minimum_quantity
):
    if is_deadline_expired(deadline_value):
        return "Abgelaufen"

    if current_quantity >= minimum_quantity:
        return "Mindestmenge erreicht"

    return "Offen"


def get_connection():
    # Datenbankdatei dealhive.db
    connection = sqlite3.connect(DATABASE_PATH)

    # dadurch können wir später auf Spaltennamen zugreifen z.B. hive["title"]
    connection.row_factory = sqlite3.Row

    # SQLite prüft Fremdschlüssel nur, wenn wir sie pro Verbindung aktivieren
    connection.execute("PRAGMA foreign_keys = ON")

    # wir geben die Verbindung zurück, damit andere Funktionen sie nutzen können
    return connection

@contextmanager
def database_transaction():
    connection = get_connection()

    try:
        yield connection
        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def create_tables():
    # hier holen wir uns eine Verbindung zur Datenbank
    connection = get_connection()

    # AUTOINCREMENT ist insane - es generiert selber IDs!!!
    # (jede Zeile bekommt eine eigene ID)
    # rest ist standart DDL oder so
    connection.execute("""
        CREATE TABLE IF NOT EXISTS hives (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            game_system TEXT NOT NULL,
            short_description TEXT NOT NULL,
            description TEXT NOT NULL,
            deadline TEXT NOT NULL,
            current_participants INTEGER NOT NULL DEFAULT 0,
            min_participants INTEGER NOT NULL,
            base_price REAL NOT NULL DEFAULT 0.0
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
            quantity INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (hive_id) REFERENCES hives(id),
            UNIQUE(user_id, hive_id, relation_type)
        )
    """)

    # Tabelle für die Preisstaffeln eines Hives
    connection.execute("""
        CREATE TABLE IF NOT EXISTS hive_tiers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hive_id INTEGER NOT NULL,
            threshold_quantity INTEGER NOT NULL,
            discount_percent REAL NOT NULL,
            FOREIGN KEY (hive_id) REFERENCES hives(id)
        )
    """)

    # Neue Tabelle für Chat-Nachrichten erstellen
    # FOREIGN KEYs stellen sicher, dass Nachrichten nur zu echten Hives
    # und Usern gehören
    connection.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hive_id INTEGER NOT NULL,
            sender_id INTEGER NOT NULL,
            receiver_id INTEGER NOT NULL,
            message_text TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (hive_id) REFERENCES hives(id),
            FOREIGN KEY (sender_id) REFERENCES users(id),
            FOREIGN KEY (receiver_id) REFERENCES users(id)
        )
    """)

    # commit fürs eigentliche Speichern
    connection.commit()
    connection.close()


def get_all_hives():
    connection = get_connection()

    # Die aktuelle Stückmenge wird direkt aus den Buyer-Bestellungen berechnet.
    # Dadurch kann der gespeicherte alte Zähler nicht von den Bestellungen
    # abweichen.
    hives = connection.execute("""
        SELECT
            hives.id,
            hives.title,
            hives.game_system,
            hives.short_description,
            hives.deadline,
            COALESCE((
                SELECT SUM(user_hives.quantity)
                FROM user_hives
                WHERE user_hives.hive_id = hives.id
                AND user_hives.relation_type = 'buyer'
            ), 0) AS current_participants,
            hives.min_participants,
            hives.base_price
        FROM hives
        ORDER BY hives.id DESC
    """).fetchall()

    connection.close()

    return hives


def get_hive_by_id(hive_id):
    connection = get_connection()

    # hier suchen wir genau einen Hive über seine ID
    # current_participants bleibt als alter Spaltenname erhalten,
    # enthält aber tatsächlich die aktuell bestellten Stücke
    hive = connection.execute("""
        SELECT
            hives.id,
            hives.title,
            hives.game_system,
            hives.short_description,
            hives.description,
            hives.deadline,
            COALESCE((
                SELECT SUM(user_hives.quantity)
                FROM user_hives
                WHERE user_hives.hive_id = hives.id
                AND user_hives.relation_type = 'buyer'
            ), 0) AS current_participants,
            hives.min_participants,
            hives.base_price
        FROM hives
        WHERE hives.id = ?
    """, (hive_id,)).fetchone()

    connection.close()

    # wir geben entweder den gefundenen Hive zurück oder "None",
    # falls nichts gefunden wurde
    return hive


def insert_hive(
    title,
    game_system,
    short_description,
    description,
    deadline,
    current_participants,
    min_participants,
    base_price=0.0
):
    connection = get_connection()

    # hier speichern wir einen neuen Hive
    # current_participants bleibt für das alte Seed-Skript erhalten
    cursor = connection.execute("""
        INSERT INTO hives (
            title,
            game_system,
            short_description,
            description,
            deadline,
            current_participants,
            min_participants,
            base_price
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        title,
        game_system,
        short_description,
        description,
        deadline,
        current_participants,
        min_participants,
        base_price
    ))

    # hier merken wir uns die ID vom gerade erstellten Hive
    new_hive_id = cursor.lastrowid

    # commit fürs eigentliche Speichern
    connection.commit()
    connection.close()

    return new_hive_id


def update_hive(
    hive_id,
    title,
    game_system,
    short_description,
    description,
    deadline,
    min_participants,
    base_price
):
    connection = get_connection()

    # hier aktualisieren wir die Grunddaten eines bestehenden Hives
    # die aktuelle Stückmenge wird aus den Bestellungen berechnet
    connection.execute("""
        UPDATE hives
        SET
            title = ?,
            game_system = ?,
            short_description = ?,
            description = ?,
            deadline = ?,
            min_participants = ?,
            base_price = ?
        WHERE id = ?
    """, (
        title,
        game_system,
        short_description,
        description,
        deadline,
        min_participants,
        base_price,
        hive_id
    ))

    connection.commit()
    connection.close()


def create_test_user(
    username,
    name,
    email,
    password_hash,
    role,
    street,
    postal_code,
    city,
    country
):
    connection = get_connection()

    # hier legen wir einen Testnutzer an, falls es ihn noch nicht gibt
    # INSERT OR IGNORE verhindert doppelte Testnutzer,
    # wenn test_database.py mehrfach läuft
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

    # danach holen wir die ID,
    # damit wir den Nutzer mit Hives verbinden können
    user = connection.execute("""
        SELECT id
        FROM users
        WHERE username = ?
    """, (username,)).fetchone()

    connection.commit()
    connection.close()

    return user["id"]


def assign_hive_to_user(user_id, hive_id, relation_type, quantity=1):
    # Nur gültige Rollen erlauben
    if relation_type not in ("creator", "buyer"):
        raise ValueError("Invalid relation_type")

    if not isinstance(quantity, int) or quantity < 1:
        raise ValueError("quantity muss mindestens 1 sein")

    connection = get_connection()

    # hier mappen wir einen User auf einen Hive
    # relation_type sagt, ob der Nutzer Creator oder Käufer dieses Hives ist
    # quantity speichert, wie viele Stück der Käufer bestellen möchte
    cursor = connection.execute("""
        INSERT OR IGNORE INTO user_hives (
            user_id,
            hive_id,
            relation_type,
            quantity
        )
        VALUES (?, ?, ?, ?)
    """, (
        user_id,
        hive_id,
        relation_type,
        quantity
    ))

    # rowcount sagt uns, ob wirklich eine neue Zuordnung entstanden ist
    relation_was_created = cursor.rowcount > 0

    connection.commit()
    connection.close()

    return relation_was_created


def get_hives_for_user(user_id, relation_type):
    if relation_type not in ("creator", "buyer"):
        raise ValueError("Invalid relation_type")

    connection = get_connection()

    # hier holen wir nur die Hives,
    # die einer bestimmten user_id zugeordnet sind
    hives = connection.execute("""
        SELECT
            hives.id,
            hives.title,
            hives.game_system,
            hives.short_description,
            hives.deadline,
            COALESCE((
                SELECT SUM(all_orders.quantity)
                FROM user_hives AS all_orders
                WHERE all_orders.hive_id = hives.id
                AND all_orders.relation_type = 'buyer'
            ), 0) AS current_participants,
            hives.min_participants,
            hives.base_price,
            user_hives.relation_type,
            user_hives.quantity
        FROM hives
        JOIN user_hives ON hives.id = user_hives.hive_id
        WHERE user_hives.user_id = ?
        AND user_hives.relation_type = ?
        ORDER BY hives.id DESC
    """, (
        user_id,
        relation_type
    )).fetchall()

    connection.close()

    return hives


def create_user(
    username,
    name,
    email,
    password_hash,
    role,
    street,
    postal_code,
    city,
    country
):
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


def get_user_by_username(username):
    connection = get_connection()

    user = connection.execute("""
        SELECT *
        FROM users
        WHERE username = ?
    """, (username,)).fetchone()

    connection.close()

    return user


def get_user_by_id(user_id):
    connection = get_connection()

    user = connection.execute("""
        SELECT *
        FROM users
        WHERE id = ?
    """, (user_id,)).fetchone()

    connection.close()

    return user


def update_user_profile(
    user_id,
    name,
    email,
    role,
    street,
    postal_code,
    city,
    country
):
    connection = get_connection()

    # hier speichern wir Änderungen am Profil des eingeloggten Nutzers
    connection.execute("""
        UPDATE users
        SET
            name = ?,
            email = ?,
            role = ?,
            street = ?,
            postal_code = ?,
            city = ?,
            country = ?
        WHERE id = ?
    """, (
        name,
        email,
        role,
        street,
        postal_code,
        city,
        country,
        user_id
    ))

    connection.commit()
    connection.close()


def save_private_message(hive_id, sender_id, receiver_id, text):
    connection = get_connection()

    connection.execute("""
        INSERT INTO messages (
            hive_id,
            sender_id,
            receiver_id,
            message_text
        )
        VALUES (?, ?, ?, ?)
    """, (
        hive_id,
        sender_id,
        receiver_id,
        text
    ))

    connection.commit()
    connection.close()


def get_private_messages(hive_id, user1_id, user2_id):
    connection = get_connection()

    # hier holen wir nur Nachrichten
    # zwischen genau diesen beiden Usern für diesen Hive
    messages = connection.execute("""
        SELECT
            messages.id,
            messages.message_text,
            messages.timestamp,
            messages.sender_id,
            users.username AS sender_name
        FROM messages
        JOIN users ON messages.sender_id = users.id
        WHERE messages.hive_id = ?
        AND (
            (messages.sender_id = ? AND messages.receiver_id = ?)
            OR
            (messages.sender_id = ? AND messages.receiver_id = ?)
        )
        ORDER BY messages.timestamp ASC
    """, (
        hive_id,
        user1_id,
        user2_id,
        user2_id,
        user1_id
    )).fetchall()

    connection.close()

    return messages


def get_hive_creator_id(hive_id):
    connection = get_connection()

    # hier holen wir den Creator,
    # der zu diesem Hive gespeichert wurde
    creator = connection.execute("""
        SELECT user_id
        FROM user_hives
        WHERE hive_id = ?
        AND relation_type = 'creator'
    """, (hive_id,)).fetchone()

    connection.close()

    if creator:
        return creator["user_id"]

    return None

def can_users_chat_in_hive(hive_id, user1_id, user2_id):
    # Niemand darf mit sich selbst chatten.
    if user1_id == user2_id:
        return False

    connection = get_connection()

    try:
        relations = connection.execute("""
            SELECT
                user_id,
                relation_type
            FROM user_hives
            WHERE hive_id = ?
            AND user_id IN (?, ?)
        """, (
            hive_id,
            user1_id,
            user2_id
        )).fetchall()

    finally:
        connection.close()

    creator_ids = {
        relation["user_id"]
        for relation in relations
        if relation["relation_type"] == "creator"
    }

    buyer_ids = {
        relation["user_id"]
        for relation in relations
        if relation["relation_type"] == "buyer"
    }

    return (
        user1_id in creator_ids
        and user2_id in buyer_ids
    ) or (
        user2_id in creator_ids
        and user1_id in buyer_ids
    )



def insert_hive_tier(hive_id, threshold_quantity, discount_percent):
    if threshold_quantity < 1:
        raise ValueError("Die Staffelmenge muss mindestens 1 sein.")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Der Rabatt muss zwischen 0 und 100 liegen.")

    connection = get_connection()

    # Speichert eine einzelne Rabattstaffel
    # für einen spezifischen Hive in der Datenbank
    connection.execute("""
        INSERT INTO hive_tiers (
            hive_id,
            threshold_quantity,
            discount_percent
        )
        VALUES (?, ?, ?)
    """, (
        hive_id,
        threshold_quantity,
        discount_percent
    ))

    connection.commit()
    connection.close()


def get_hive_tiers(hive_id):
    connection = get_connection()

    # Holt alle Rabattstaffeln eines Hives aus der Datenbank,
    # sortiert nach der Mindestmenge aufsteigend
    tiers = connection.execute("""
        SELECT
            threshold_quantity,
            discount_percent
        FROM hive_tiers
        WHERE hive_id = ?
        ORDER BY threshold_quantity ASC
    """, (hive_id,)).fetchall()

    connection.close()

    return tiers


def replace_hive_tiers(hive_id, thresholds, discounts):
    connection = get_connection()

    try:
        # hier löschen wir zuerst die alten Preisstufen dieses Hives
        # danach speichern wir die bereits geprüften Werte neu
        connection.execute("""
            DELETE FROM hive_tiers
            WHERE hive_id = ?
        """, (hive_id,))

        for threshold_quantity, discount_percent in zip(
            thresholds,
            discounts
        ):
            connection.execute("""
                INSERT INTO hive_tiers (
                    hive_id,
                    threshold_quantity,
                    discount_percent
                )
                VALUES (?, ?, ?)
            """, (
                hive_id,
                threshold_quantity,
                discount_percent
            ))

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def calculate_current_price(hive_id):
    # Berechnet den aktuellen, dynamischen Preis pro Stück
    # basierend auf den Gesamtbestellungen und Rabattstaffeln
    hive = get_hive_by_id(hive_id)

    if not hive:
        return 0.0

    base_price = hive["base_price"]
    current_total = hive["current_participants"]
    tiers = get_hive_tiers(hive_id)

    active_discount = 0.0

    # Wir verwenden immer den höchsten bereits erreichten Rabatt.
    # Dadurch kann der Preis bei einer höheren Bestellmenge niemals wieder steigen.
    for tier in tiers:
        if current_total >= tier["threshold_quantity"]:
            active_discount = max(
                active_discount,
                tier["discount_percent"]
            )

    # Endpreis berechnen z.B. 50.00 * (1.0 - 0.10) = 45.00
    current_price = base_price * (1.0 - (active_discount / 100.0))

    return round(current_price, 2)


def get_buyers_for_hive(hive_id):
    connection = get_connection()

    # Holt alle User,
    # die als 'buyer' mit diesem Hive verknüpft sind
    buyers = connection.execute("""
        SELECT
            users.id,
            users.username,
            users.name,
            users.email,
            users.city,
            users.country,
            user_hives.quantity
        FROM users
        JOIN user_hives ON users.id = user_hives.user_id
        WHERE user_hives.hive_id = ?
        AND user_hives.relation_type = 'buyer'
        ORDER BY users.username ASC
    """, (hive_id,)).fetchall()

    connection.close()

    return buyers


def create_hive_with_tiers(
    creator_id,
    title,
    game_system,
    short_description,
    description,
    deadline,
    min_participants,
    base_price,
    tiers
):
    # Hive, Creator-Zuordnung und Rabattstaffeln werden
    # vollständig in derselben Transaktion gespeichert.
    with database_transaction() as connection:
        cursor = connection.execute("""
            INSERT INTO hives (
                title,
                game_system,
                short_description,
                description,
                deadline,
                current_participants,
                min_participants,
                base_price
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            title,
            game_system,
            short_description,
            description,
            deadline,
            0,
            min_participants,
            base_price
        ))

        new_hive_id = cursor.lastrowid

        connection.execute("""
            INSERT INTO user_hives (
                user_id,
                hive_id,
                relation_type,
                quantity
            )
            VALUES (?, ?, ?, ?)
        """, (
            creator_id,
            new_hive_id,
            "creator",
            1
        ))

        connection.executemany("""
            INSERT INTO hive_tiers (
                hive_id,
                threshold_quantity,
                discount_percent
            )
            VALUES (?, ?, ?)
        """, [
            (
                new_hive_id,
                threshold,
                discount
            )
            for threshold, discount in tiers
        ])

    return new_hive_id