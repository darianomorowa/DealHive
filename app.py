import sqlite3
from flask import Flask, render_template, request, redirect
from database import create_tables, get_all_hives, get_hive_by_id

app = Flask(__name__)

# hier erstellen wir beim Start der App die Tabelle, falls sie noch nicht existiert
create_tables()

@app.route("/")
def home():
    return "meine erste kleine Seite hehehe"

@app.route("/hives")
def hives_overview():
    # hier holen wir die Hives aus der Datenbank
    hives = get_all_hives()

    # html variable
    html = "<h1>Hives entdecken</h1>"

    # Schleife für alle Hives mit Detaillink für jeden Hive
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
    # hier holen wir genau den einen =ID Hive aus der Datenbank
    hive = get_hive_by_id(hive_id)

    # falls es keinen Hive mit dieser ID gibt, zeigen wir erstmal eine einfache Meldung
    if hive is None:
        return "Hive wurde nicht gefunden."
    
    return f"""
    <h1>{hive["title"]}</h1>
    <p>ID: {hive["id"]}</p>
    <a href="/hives">Zurück zu allen Hives</a>
    """

# Zeigt das Formular an, mit dem ein Creator einen neuen Hive erstellen kann
@app.route("/creator/hives/new", methods=["GET", "POST"])
def create_hive_page():
    
    # Wenn der Nutzer das Formular abschickt (POST)
    if request.method == "POST":
        
        # 1. Alle Daten aus dem Formular auslesen
        title = request.form.get("title")
        category = request.form.get("category")
        game_system = request.form.get("game_system")
        material = request.form.get("material")
        description = request.form.get("description")
        base_price = request.form.get("base_price")
        min_participants = request.form.get("min_participants")
        deadline = request.form.get("deadline")
        
        # 2. Direkt in die SQLite-Datenbank speichern
        # (Hinweis: 'dealhive.db' ist der Standardname, falls in database.py nichts anderes steht)
        conn = sqlite3.connect("dealhive.db")
        cursor = conn.cursor()
        
        # Wir stellen sicher, dass die Zwischentabelle existiert, falls Mathieu sie noch nicht angelegt hat
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_hives (
                user_id INTEGER NOT NULL,
                hive_id INTEGER NOT NULL,
                if_creator BOOLEAN NOT NULL CHECK (if_creator IN (0, 1)),
                PRIMARY KEY (user_id, hive_id)
            )
        ''')
        
        # Hive in die 'hives' Tabelle einfügen
        cursor.execute('''
            INSERT INTO hives (title, game_system, deadline, min_participants, category, material, description, base_price)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (title, game_system, deadline, min_participants, category, material, description, base_price))
        
        # Die ID des gerade eben erstellten Hives holen
        last_hive_id = cursor.lastrowid
        
        # Daniels Extra-Tabelle befüllen (Verknüpfung User <-> Hive):
        # Wir simulieren, dass der aktuell eingeloggte Creator die User-ID 1 hat
        simulierte_user_id = 1 
        cursor.execute('''
            INSERT INTO user_hives (user_id, hive_id, if_creator)
            VALUES (?, ?, ?)
        ''', (simulierte_user_id, last_hive_id, 1)) # 1 steht für True
        
        conn.commit()
        conn.close()
        
        # 3. Weiterleitung auf die Übersichtsseite
        return redirect("/hives")

    # Wenn der Nutzer die Seite nur normal aufruft (GET), zeige das leere Formular
    return render_template("create_hive.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)