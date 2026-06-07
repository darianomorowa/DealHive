from flask import Flask, render_template, request
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
    # hier holen wir genau den einen =ID Hive aus der Datenbank
    hive = get_hive_by_id(hive_id)

    # falls es keinen Hive mit dieser ID gibt, zeigen wir erstmal eine einfache Meldung
    if hive is None:
        return "Hive wurde nicht gefunden."

    
    return f"""
    <h1>{hive["title"]}</h1>

    <p>ID: {hive["id"]}</p>
    <p>Deadline: {hive["deadline"]}</p>
    <p>Teilnehmer: {hive["current_participants"]} / {hive["min_participants"]}</p>

    <a href="/hives">Zurück zu allen Hives</a>
    """

if __name__ == "__main__":
    app.run(debug=True)