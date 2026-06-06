from flask import Flask, render_template
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
@app.route("/creator/hives/new")
def create_hive_page():
    
    return render_template("create_hive.html")
if __name__ == "__main__":
    app.run(debug=True, port=5001)