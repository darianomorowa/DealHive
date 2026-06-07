from flask import Flask, render_template, request
from database import create_tables, get_all_hives, get_hive_by_id
from creator_routes import register_creator_routes

app = Flask(__name__)

# Datenbanktabellen beim Start der App initialisieren
create_tables()

# hier registrieren wir die Creator-Routen aus creator_routes.py
register_creator_routes(app)


@app.route("/")
def home():
    return "meine erste kleine Seite hehehe"


@app.route("/hives")
def hives_overview():
    # Alle bestehenden Hives aus der Datenbank abrufen
    hives = get_all_hives()

    #variable für "welches System" - Filter
    selected_game_system = request.args.get("game_system", "all")

    # leere Liste, wo später hives abgespeichert werden
    filtered_hives = []

    # wir gehen jeden Hive durch und prüfen, ob er angezeigt werden soll
    for hive in hives:
        # bei "all" zeigen wir einfach alles an
        if selected_game_system == "all":
            filtered_hives.append(hive)

        # sonst prüfen wir, ob das Spielsystem vom Hive zum Filter passt
        elif hive["game_system"] == selected_game_system:
            filtered_hives.append(hive)

    # hier geben wir die gefilterten Hives und den aktuellen Filter
    # ans Template weiter
    return render_template(
        "hives.html",
        hives=filtered_hives,
        selected_game_system=selected_game_system
    )


#Detailroute
@app.route("/hives/<int:hive_id>")
def hive_detail(hive_id):
    # Spezifischen Hive anhand der ID aus der Datenbank auslesen
    hive = get_hive_by_id(hive_id)

    # Fehlerbehandlung: Falls die ID nicht existiert
    if hive is None:
        return "Hive wurde nicht gefunden."

    # hier geben wir den gefundenen Hive an die Detail-HTML-Datei weiter
    return render_template("hive_detail.html", hive=hive)


if __name__ == "__main__":
    app.run(debug=True)