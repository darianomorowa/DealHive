from flask import render_template, request, redirect, session
from database import insert_hive, get_hives_for_user, assign_hive_to_user, insert_hive_tier

def register_creator_routes(app):
    @app.route("/creator/hives/new", methods=["GET", "POST"])
    def create_hive_page():

        if session.get("user_id") is None:
            return redirect("/login")

        if session.get("role") != "creator":
            return redirect("/")
        
        # Standard: Beim ersten Aufruf der Seite starten wir mit einer leeren Zeile
        thresholds = [""]
        discounts = [""]

        # Verarbeitung der eingegebenen Daten, wenn das Formular abgeschickt wurde
        if request.method == "POST":
            # Wir lesen aus, welcher Button geklickt wurde ('add_tier' or 'submit')
            action = request.form.get("action")

            # Die bisher eingetippten Staffeln auslesen, damit sie nicht verloren gehen
            thresholds = request.form.getlist("threshold_quantity[]")
            discounts = request.form.getlist("discount_percent[]")

            # FALL A: Der User hat auf "+ Weitere Staffel hinzufügen" geklickt
            if action == "add_tier":
                # Wir hängen einfach ein leeres Feld an die Listen an
                thresholds.append("")
                discounts.append("")
                # Wir rendern die Seite neu mit der zusätzlichen Zeile und ALLEN bisherigen Eingaben!
                return render_template(
                    "create_hive.html", 
                    thresholds=thresholds, 
                    discounts=discounts,
                    title=request.form.get("title", ""),
                    game_system=request.form.get("game_system", ""),
                    short_description=request.form.get("short_description", ""),
                    description=request.form.get("description", ""),
                    min_participants=request.form.get("min_participants", ""),
                    base_price=request.form.get("base_price", ""),
                    deadline=request.form.get("deadline", "")
                )
          
            # FALL B: Der User klickt auf "Hive erstellen" (Finales Speichern)
            elif action == "submit":
                title = request.form.get("title")
                game_system = request.form.get("game_system")
                short_description = request.form.get("short_description")
                description = request.form.get("description")
                min_participants = request.form.get("min_participants")
                deadline = request.form.get("deadline")
                base_price = float(request.form.get("base_price", 0.0))

                # Neue Hives starten erstmal mit 0 Teilnehmern
                current_participants = 0

                # Den neuen Datensatz über database.py in die zentrale hives-Tabelle schreiben
                new_hive_id = insert_hive(
                    title,
                    game_system,
                    short_description,
                    description,
                    deadline,
                    current_participants,
                    min_participants,
                    base_price
                )

                # Hier ordnen wir den neu erstellten Hive direkt dem eingeloggten Creator zu
                assign_hive_to_user(session["user_id"], new_hive_id, "creator")

                # Schleife verknüpft die Listen und speichert jede gültige Staffel in der DB
                for i in range(len(thresholds)):
                    if thresholds[i] and discounts[i]:
                        insert_hive_tier(new_hive_id, int(thresholds[i]), float(discounts[i]))

                # Nach erfolgreichem Speichern den Nutzer zum Creator Dashboard umleiten
                return redirect("/creator/dashboard")

        # Rendert das leere Formular, wenn die Seite normal aufgerufen wird (GET-Anfrage)
        return render_template("create_hive.html", thresholds=thresholds, discounts=discounts)
    
    @app.route("/creator/dashboard")
    def creator_dashboard():
        if session.get("user_id") is None:
            return redirect("/login")

        if session.get("role") != "creator":
            return redirect("/")

        hives = get_hives_for_user(session["user_id"], "creator")

        return render_template(
            "creator_dashboard.html",
            hives=hives
        )