from flask import render_template, request, redirect, session
from database import insert_hive, get_hives_for_user, assign_hive_to_user, insert_hive_tier

def register_creator_routes(app):
    @app.route("/creator/hives/new", methods=["GET", "POST"])
    def create_hive_page():

        if session.get("user_id") is None:
            return redirect("/login")

        if session.get("role") != "creator":
            return redirect("/")
        # Verarbeitung der eingegebenen Daten, wenn das Formular abgeschickt wurde
        if request.method == "POST":

            # 1. Auslesen der Input-Felder aus dem HTML-Formular
            title = request.form.get("title")
            game_system = request.form.get("game_system")
            short_description = request.form.get("short_description")
            description = request.form.get("description")
            min_participants = request.form.get("min_participants")
            deadline = request.form.get("deadline")

            # neu Basispreis auslesen und in eine Fließkommazahl umwandeln
            base_price = float(request.form.get("base_price", 0.0))

            # 2. Neue Hives starten erstmal mit 0 Teilnehmern
            current_participants = 0

            # 3. Den neuen Datensatz über database.py in die zentrale hives-Tabelle schreiben
            new_hive_id = insert_hive(
                title,
                game_system,
                short_description,
                description,
                deadline,
                current_participants,
                min_participants
                base_price
            )

            # hier ordnen wir den neu erstellten Hive direkt dem eingeloggten Creator zu
            assign_hive_to_user(session["user_id"], new_hive_id, "creator")

            # neu Dynamische Staffeln aus dem Formular auslesen
            thresholds = request.form.getlist("threshold_quantity[]")
            discounts = request.form.getlist("discount_percent[]")

            # Schleife verknüpft die Listen und speichert jede gültige Staffel in der DB
            for i in range(len(thresholds)):
                if thresholds[i] and discounts[i]:
                    insert_hive_tier(new_hive_id, int(thresholds[i]), float(discounts[i]))

            # 4. Nach erfolgreichem Speichern den Nutzer zum Creator Dashboard umleiten
            return redirect("/creator/dashboard")

        # Rendert das leere Formular, wenn die Seite normal aufgerufen wird (GET-Anfrage)
        return render_template("create_hive.html")
    
    @app.route("/creator/dashboard")
    def creator_dashboard():
        # ohne Login soll niemand das Creator Dashboard sehen
        if session.get("user_id") is None:
            return redirect("/login")

        # wenn man nicht in der Creator-Ansicht ist, geht es zurück zur Startseite
        if session.get("role") != "creator":
            return redirect("/")

        # hier laden wir nur die Hives, die dem eingeloggten Creator zugeordnet sind
        hives = get_hives_for_user(session["user_id"], "creator")

        return render_template(
            "creator_dashboard.html",
            hives=hives
        )

