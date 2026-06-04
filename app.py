from flask import Flask
from database import create_tables, get_all_hives

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
        </div>
        <hr>
        """

    return html

if __name__ == "__main__":
    app.run(debug=True)