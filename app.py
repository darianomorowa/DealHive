import sqlite3
from flask import Flask, render_template, request, redirect
from database import create_tables, get_all_hives, get_hive_by_id

app = Flask(__name__)

# Datenbanktabellen beim Start der App initialisieren
create_tables()

@app.route("/")
def home():
    return "meine erste kleine Seite hehehe"

@app.route("/hives")
def hives_overview():
    # Alle bestehenden Hives aus der Datenbank abrufen
    hives = get_all_hives()
    html = "<h1>Hives entdecken</h1>"

    # Dynamische HTML-Liste für die Übersicht generieren
    for hive in hives:
        html += f"""
        <div>
            <h2>{hive["title"]}</h2>
            <p>ID: {hive["id"]}</p>
            <a href="/hives/{hive["id"]}">Details ansehen</a>
        </div>
        <hr>
        """
    return html

@app.route("/hives/<int:hive_id>")
def hive_detail(hive_id):
    # Spezifischen Hive anhand der ID aus der Datenbank auslesen
    hive = get_hive_by_id(hive_id)
    
    # Fehlerbehandlung: Falls die ID nicht existiert
    if hive is None:
        return "Hive wurde nicht gefunden."
    
    return f"""
    <h1>{hive["title"]}</h1>
    <p>ID: {hive["id"]}</p>
    <a href="/hives">Zurück zu allen Hives</a>
    """

@app.route("/creator/hives/new", methods=["GET", "POST"])
def create_hive_page():
    # Verarbeitung der eingegebenen Daten, wenn das Formular abgeschickt wurde
    if request.method == "POST":
        
        # 1. Auslesen der Input-Felder aus dem HTML-Formular
        title = request.form.get("title")
        category = request.form.get("category")
        game_system = request.form.get("game_system")
        material = request.form.get("material")
        description = request.form.get("description")
        base_price = request.form.get("base_price")
        min_participants = request.form.get("min_participants")
        deadline = request.form.get("deadline")
        
        # 2. Verbindung zur lokalen SQLite-Datenbank herstellen
        conn = sqlite3.connect("dealhive.db")
        cursor = conn.cursor()
        
        # 3. Zwischentabelle für die n:m-Beziehung (User <-> Hive) anlegen, falls noch nicht existent
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_hives (
                user_id INTEGER NOT NULL,
                hive_id INTEGER NOT NULL,
                if_creator BOOLEAN NOT NULL CHECK (if_creator IN (0, 1)),
                PRIMARY KEY (user_id, hive_id)
            )
        ''')
        
        # 4. Den neuen Datensatz in die zentrale 'hives'-Tabelle schreiben
        cursor.execute('''
            INSERT INTO hives (title, game_system, deadline, min_participants, category, material, description, base_price)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (title, game_system, deadline, min_participants, category, material, description, base_price))
        
        # 5. Die automatisch generierte ID des soeben erstellten Hives abfangen
        last_hive_id = cursor.lastrowid
        
        # 6. Verknüpfung in der Zwischentabelle setzen (Zuweisung des Erstellers via Dummy-User-ID 1)
        simulierte_user_id = 1 
        cursor.execute('''
            INSERT INTO user_hives (user_id, hive_id, if_creator)
            VALUES (?, ?, ?)
        ''', (simulierte_user_id, last_hive_id, 1))
        
        # 7. Transaktion bestätigen und Verbindung sauber schließen
        conn.commit()
        conn.close()
        
        # 8. Nach erfolgreichem Speichern den Nutzer zur Übersicht umleiten
        return redirect("/hives")

    # Rendert das leere Formular, wenn die Seite normal aufgerufen wird (GET-Anfrage)
    return render_template("create_hive.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)