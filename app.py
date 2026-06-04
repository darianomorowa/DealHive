from flask import Flask
from database import create_tables, get_all_hives
from database import create_tables, get_all_hives, get_hive_by_id

app = Flask(__name__)


@app.route("/")
def home():
    return "meine erste kleine Seite hehehe"

@app.route("/hives")
def hives_overview():
    # hier stellen wir sicher, dass die Tabelle existiert
    create_tables()

    # hier holen wir die Hives aus der Datenbank
    hives = get_all_hives()

    # erstmal simples HTML direkt hier, damit die Logik sichtbar bleibt
    html = "<h1>Hives entdecken</h1>"

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
    # hier holen wir genau einen Hive aus der Datenbank
    hive = get_hive_by_id(hive_id)

    # falls es keinen Hive mit dieser ID gibt, zeigen wir erstmal eine einfache Meldung
    if hive is None:
        return "Hive wurde nicht gefunden."

    # erstmal simples HTML direkt hier, damit die Logik sichtbar bleibt
    return f"""
    <h1>{hive["title"]}</h1>
    <p>ID: {hive["id"]}</p>
    <a href="/hives">Zurück zu allen Hives</a>
    """

if __name__ == "__main__":
    app.run(debug=True)