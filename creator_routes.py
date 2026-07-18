from pricing_logic import active_discount_was_lowered
from flask import render_template, request, redirect, session
from database import (
    insert_hive,
    get_hives_for_user,
    assign_hive_to_user,
    insert_hive_tier,
    get_hive_by_id,
    get_hive_creator_id,
    update_hive,
    get_hive_tiers,
    replace_hive_tiers
)

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
    

    @app.route("/creator/hives/<int:hive_id>/edit", methods=["GET", "POST"])
    def edit_hive_page(hive_id):
        if session.get("user_id") is None:
            return redirect("/login")

        if session.get("role") != "creator":
            return redirect("/")

        hive = get_hive_by_id(hive_id)

        if hive is None:
            return "Hive wurde nicht gefunden."

        creator_id = get_hive_creator_id(hive_id)

        # hier prüfen wir, ob der eingeloggte Nutzer wirklich der Creator dieses Hives ist
        if creator_id != session["user_id"]:
            return redirect("/creator/dashboard")

        # hier holen wir die bisherigen Rabattstaffeln aus der Datenbank
        tiers = get_hive_tiers(hive_id)

        thresholds = []
        discounts = []
        locked_tiers = []

        # hier bereiten wir die alten Preisstaffeln für das Formular vor
        for tier in tiers:
            threshold = tier["threshold_quantity"]
            discount = tier["discount_percent"]

            thresholds.append(threshold)
            discounts.append(discount)

            # wenn die aktuelle Menge die Staffel schon erreicht hat,
            # soll diese Staffel im Formular nicht mehr bearbeitet werden
            if hive["current_participants"] >= threshold:
                locked_tiers.append(True)
            else:
                locked_tiers.append(False)

        # wenn noch keine Staffel existiert, zeigen wir trotzdem eine leere Zeile
        if not thresholds:
            thresholds = [""]
            discounts = [""]
            locked_tiers = [False]

        if request.method == "POST":
            action = request.form.get("action")

            title = request.form.get("title")
            game_system = request.form.get("game_system")
            short_description = request.form.get("short_description")
            description = request.form.get("description")
            deadline = request.form.get("deadline")
            min_participants = int(request.form.get("min_participants"))
            base_price = float(request.form.get("base_price", 0.0))

            # hier lesen wir alle Staffeln aus dem Formular neu ein
            thresholds = request.form.getlist("threshold_quantity[]")
            discounts = request.form.getlist("discount_percent[]")
            locked_tiers_raw = request.form.getlist("locked_tier[]")

            locked_tiers = []

            # hidden inputs kommen als "true" oder "false" aus dem Formular zurück
            for value in locked_tiers_raw:
                if value == "true":
                    locked_tiers.append(True)
                else:
                    locked_tiers.append(False)

            # wenn der Nutzer nur eine weitere Zeile hinzufügen will,
            # speichern wir noch nicht, sondern rendern das Formular neu
            if action == "add_tier":
                thresholds.append("")
                discounts.append("")
                locked_tiers.append(False)

                return render_template(
                    "edit_hive.html",
                    hive=hive,
                    thresholds=thresholds,
                    discounts=discounts,
                    locked_tiers=locked_tiers,
                    title=title,
                    game_system=game_system,
                    short_description=short_description,
                    description=description,
                    min_participants=min_participants,
                    base_price=base_price,
                    deadline=deadline
                )

            # hier speichern wir die normalen Hive-Daten
            update_hive(
                hive_id,
                title,
                game_system,
                short_description,
                description,
                deadline,
                min_participants,
                base_price
            )

            # hier ersetzen wir die Rabattstaffeln durch die Werte aus dem Formular
            # erreichte Staffeln bleiben erhalten, weil sie readonly angezeigt und trotzdem mitgeschickt werden
            replace_hive_tiers(hive_id, thresholds, discounts)

            return redirect("/creator/dashboard")

        return render_template(
            "edit_hive.html",
            hive=hive,
            thresholds=thresholds,
            discounts=discounts,
            locked_tiers=locked_tiers
        )
        
    @app.route("/creator/hives/<int:hive_id>/buyers")
    def view_hive_buyers(hive_id):
        if session.get("user_id") is None:
            return redirect("/login")

        if session.get("role") != "creator":
            return redirect("/")

        hive = get_hive_by_id(hive_id)
        if hive is None:
            return "Hive wurde nicht gefunden."

        creator_id = get_hive_creator_id(hive_id)
        if creator_id != session["user_id"]:
            return redirect("/creator/dashboard")

        from database import get_buyers_for_hive
        buyers = get_buyers_for_hive(hive_id)

        return render_template("hive_buyers.html", hive=hive, buyers=buyers)
        