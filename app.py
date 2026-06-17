from flask import Flask, render_template, request, redirect, abort
from database import (
    create_tables,
    get_hive_by_id,
    update_hive,
    is_creator_of_hive,
    get_hives_for_user
)
from creator_routes import register_creator_routes
from user_routes import setup_user_routes
from hives import register_hive_routes

# Zugriff auf unsere Projektbilder ermöglichen
app = Flask(__name__, static_folder="docs/assets", static_url_path="/assets")

# secret_key brauchen wir, damit Flask Sessions speichern kann
# da wir nur mit Testdaten arbeiten kann auf komplexe Sicherheit vorerst verzichtet werden
app.secret_key = "dealhive-dev-secret-key"

# Datenbanktabellen beim Start der App initialisieren
create_tables()

# hier registrieren wir die Creator-Routen aus creator_routes.py
register_creator_routes(app)

# nutzer-routen laden
setup_user_routes(app)

# hier registrieren wir die Hive-Routen aus hives.py
register_hive_routes(app)


@app.route("/")
def home():
    # hier landet der Nutzer auf der Startseite
    # nach Login oder Registrierung leiten wir später auch hierhin zurück
    return render_template("home.html")


@app.route("/dashboard")
def user_dashboard():
    # aktuell hardcoded zum Testen
    # später ersetzen wir das durch: user_id = session["user_id"]
    user_id = 1

    # hier laden wir alle Hives, denen der Demo-Buyer beigetreten ist
    joined_hives = get_hives_for_user(user_id, "buyer")

    return render_template("dashboard.html", hives=joined_hives)


@app.route("/creator/hives/<int:hive_id>/edit", methods=["GET", "POST"])
def edit_hive(hive_id):
    # aktuell hardcoded zum Testen
    # später ersetzen wir das durch: user_id = session["user_id"]
    user_id = 0

    # erst prüfen wir, ob dieser User Creator von diesem Hive ist
    if not is_creator_of_hive(user_id, hive_id):
        abort(403)

    # Hive aus der Datenbank laden
    hive = get_hive_by_id(hive_id)

    # falls es den Hive nicht gibt, zeigen wir 404
    if hive is None:
        abort(404)

    # POST bedeutet: Formular wurde abgeschickt, Änderungen speichern
    if request.method == "POST":
        title = request.form["title"]
        game_system = request.form["game_system"]
        short_description = request.form["short_description"]
        description = request.form["description"]
        deadline = request.form["deadline"]
        min_participants = int(request.form["min_participants"])

        update_hive(
            hive_id,
            title,
            game_system,
            short_description,
            description,
            deadline,
            min_participants
        )

        return redirect(f"/hives/{hive_id}")

    # GET bedeutet: Bearbeitungsformular anzeigen
    return render_template("edit_hive.html", hive=hive)


if __name__ == "__main__":
    app.run(debug=True, port=5001)