from flask import render_template, request, redirect
from database import insert_hive, get_hives_for_user
from flask import render_template, request, redirect
from database import insert_hive


def register_creator_routes(app):
    @app.route("/creator/hives/new", methods=["GET", "POST"])
    def create_hive_page():
        # Verarbeitung der eingegebenen Daten, wenn das Formular abgeschickt wurde
        if request.method == "POST":

            # 1. Auslesen der Input-Felder aus dem HTML-Formular
            title = request.form.get("title")
            game_system = request.form.get("game_system")
            short_description = request.form.get("short_description")
            description = request.form.get("description")
            min_participants = request.form.get("min_participants")
            deadline = request.form.get("deadline")

            # 2. Neue Hives starten erstmal mit 0 Teilnehmern
            current_participants = 0

            # 3. Den neuen Datensatz über database.py in die zentrale hives-Tabelle schreiben
            insert_hive(
                title,
                game_system,
                short_description,
                description,
                deadline,
                current_participants,
                min_participants
            )

            # 4. Nach erfolgreichem Speichern den Nutzer zur Übersicht umleiten
            return redirect("/hives")

        # Rendert das leere Formular, wenn die Seite normal aufgerufen wird (GET-Anfrage)
        return render_template("create_hive.html")
    
    @app.route("/creator/dashboard")
    def creator_dashboard():
        # erstmal hardcoded, weil wir noch kein richtiges Login haben
        # user_id 0 ist unser Demo-Creator für die Präsentation
        demo_creator_id = 0

        # hier laden wir nur die Hives, die dem Demo-Creator zugeordnet sind
        hives = get_hives_for_user(demo_creator_id, "creator")

        return render_template(
            "creator_dashboard.html",
            hives=hives
        )

