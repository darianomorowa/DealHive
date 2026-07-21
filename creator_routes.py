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
    replace_hive_tiers,
    get_hive_status
)


# prüft, ob die eingegebenen Rabattstaffeln logisch aufgebaut sind
def validate_tiers(thresholds, discounts):
    if len(thresholds) != len(discounts):
        return "Die Rabattstaffeln konnten nicht verarbeitet werden.", None

    validated_tiers = []

    previous_threshold = None
    previous_discount = None

    for threshold_value, discount_value in zip(thresholds, discounts):
        threshold_value = threshold_value.strip()
        discount_value = discount_value.strip()

        # eine vollständig leere Zeile wird ignoriert
        if not threshold_value and not discount_value:
            continue

        # eine Staffel muss immer Menge und Rabatt enthalten
        if not threshold_value or not discount_value:
            return (
                "Bitte gib bei jeder Rabattstaffel sowohl eine Stückzahl "
                "als auch einen Rabatt ein.",
                None
            )

        try:
            threshold = int(threshold_value)
            discount = float(discount_value)
        except ValueError:
            return (
                "Stückzahl und Rabatt müssen gültige Zahlen sein.",
                None
            )

        if threshold < 1:
            return (
                "Die Stückzahl einer Rabattstaffel muss mindestens 1 betragen.",
                None
            )

        if discount < 0 or discount > 100:
            return (
                "Der Rabatt muss zwischen 0 und 100 Prozent liegen.",
                None
            )

        if previous_threshold is not None and threshold <= previous_threshold:
            return (
                "Die Stückzahlen der Rabattstaffeln müssen aufsteigend sein.",
                None
            )

        if previous_discount is not None and discount < previous_discount:
            return (
                "Mit steigender Bestellmenge darf der Rabatt nicht kleiner werden.",
                None
            )

        validated_tiers.append((threshold, discount))

        previous_threshold = threshold
        previous_discount = discount

    return None, validated_tiers


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

            # Wir lesen aus, welcher Button geklickt wurde
            action = request.form.get("action")

            # Die bisher eingetippten Staffeln auslesen,
            # damit sie nicht verloren gehen
            thresholds = request.form.getlist("threshold_quantity[]")
            discounts = request.form.getlist("discount_percent[]")

            title = request.form.get("title", "")
            game_system = request.form.get("game_system", "")
            short_description = request.form.get("short_description", "")
            description = request.form.get("description", "")
            min_participants = request.form.get("min_participants", "")
            base_price = request.form.get("base_price", "")
            deadline = request.form.get("deadline", "")

            # FALL A: Der User hat auf
            # "+ Weitere Staffel hinzufügen" geklickt
            if action == "add_tier":

                # Wir hängen einfach ein leeres Feld an die Listen an
                thresholds.append("")
                discounts.append("")

                # Wir rendern die Seite neu mit der zusätzlichen Zeile
                # und allen bisherigen Eingaben
                return render_template(
                    "create_hive.html",
                    thresholds=thresholds,
                    discounts=discounts,
                    title=title,
                    game_system=game_system,
                    short_description=short_description,
                    description=description,
                    min_participants=min_participants,
                    base_price=base_price,
                    deadline=deadline
                )

            # FALL B: Der User klickt auf "Hive erstellen"
            elif action == "submit":

                try:
                    min_participants_number = int(min_participants)
                    base_price_number = float(base_price)
                except ValueError:
                    return render_template(
                        "create_hive.html",
                        thresholds=thresholds,
                        discounts=discounts,
                        title=title,
                        game_system=game_system,
                        short_description=short_description,
                        description=description,
                        min_participants=min_participants,
                        base_price=base_price,
                        deadline=deadline,
                        error_message=(
                            "Mindestmenge und Basispreis müssen "
                            "gültige Zahlen sein."
                        )
                    )

                if min_participants_number < 1:
                    return render_template(
                        "create_hive.html",
                        thresholds=thresholds,
                        discounts=discounts,
                        title=title,
                        game_system=game_system,
                        short_description=short_description,
                        description=description,
                        min_participants=min_participants,
                        base_price=base_price,
                        deadline=deadline,
                        error_message=(
                            "Die Mindestmenge muss mindestens 1 betragen."
                        )
                    )

                if base_price_number < 0:
                    return render_template(
                        "create_hive.html",
                        thresholds=thresholds,
                        discounts=discounts,
                        title=title,
                        game_system=game_system,
                        short_description=short_description,
                        description=description,
                        min_participants=min_participants,
                        base_price=base_price,
                        deadline=deadline,
                        error_message=(
                            "Der Basispreis darf nicht negativ sein."
                        )
                    )

                validation_error, validated_tiers = validate_tiers(
                    thresholds,
                    discounts
                )

                if validation_error:
                    return render_template(
                        "create_hive.html",
                        thresholds=thresholds,
                        discounts=discounts,
                        title=title,
                        game_system=game_system,
                        short_description=short_description,
                        description=description,
                        min_participants=min_participants,
                        base_price=base_price,
                        deadline=deadline,
                        error_message=validation_error
                    )

                # Neue Hives starten mit einer Bestellmenge von 0
                current_participants = 0

                # Den neuen Datensatz über database.py
                # in die zentrale hives-Tabelle schreiben
                new_hive_id = insert_hive(
                    title,
                    game_system,
                    short_description,
                    description,
                    deadline,
                    current_participants,
                    min_participants_number,
                    base_price_number
                )

                # Den neu erstellten Hive direkt
                # dem eingeloggten Creator zuordnen
                assign_hive_to_user(
                    session["user_id"],
                    new_hive_id,
                    "creator"
                )

                # Alle geprüften Rabattstaffeln speichern
                for threshold, discount in validated_tiers:
                    insert_hive_tier(
                        new_hive_id,
                        threshold,
                        discount
                    )

                # Nach erfolgreichem Speichern
                # zum Creator Dashboard umleiten
                return redirect("/creator/dashboard")

        # Leeres Formular bei einer normalen GET-Anfrage
        return render_template(
            "create_hive.html",
            thresholds=thresholds,
            discounts=discounts
        )


    @app.route("/creator/dashboard")
    def creator_dashboard():

        if session.get("user_id") is None:
            return redirect("/login")

        if session.get("role") != "creator":
            return redirect("/")

        hives = get_hives_for_user(
            session["user_id"],
            "creator"
        )

        hives_with_status = []

        for hive in hives:
            hive_data = dict(hive)

            hive_data["status"] = get_hive_status(
                hive["deadline"],
                hive["current_participants"],
                hive["min_participants"]
            )

            hives_with_status.append(hive_data)

        return render_template(
            "creator_dashboard.html",
            hives=hives_with_status
        )

    @app.route(
        "/creator/hives/<int:hive_id>/edit",
        methods=["GET", "POST"]
    )
    def edit_hive_page(hive_id):

        if session.get("user_id") is None:
            return redirect("/login")

        if session.get("role") != "creator":
            return redirect("/")

        hive = get_hive_by_id(hive_id)

        if hive is None:
            return "Hive wurde nicht gefunden."

        creator_id = get_hive_creator_id(hive_id)

        # hier prüfen wir, ob der eingeloggte Nutzer
        # wirklich der Creator dieses Hives ist
        if creator_id != session["user_id"]:
            return redirect("/creator/dashboard")

        # hier holen wir die bisherigen Rabattstaffeln
        # aus der Datenbank
        tiers = get_hive_tiers(hive_id)

        thresholds = []
        discounts = []
        locked_tiers = []

        # hier bereiten wir die alten Preisstaffeln
        # für das Formular vor
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

        # wenn noch keine Staffel existiert,
        # zeigen wir trotzdem eine leere Zeile
        if not thresholds:
            thresholds = [""]
            discounts = [""]
            locked_tiers = [False]

        if request.method == "POST":

            action = request.form.get("action")

            title = request.form.get("title", "")
            game_system = request.form.get("game_system", "")
            short_description = request.form.get(
                "short_description",
                ""
            )
            description = request.form.get("description", "")
            deadline = request.form.get("deadline", "")
            min_participants = request.form.get(
                "min_participants",
                ""
            )
            base_price = request.form.get("base_price", "")

            # hier lesen wir alle Staffeln
            # aus dem Formular neu ein
            thresholds = request.form.getlist(
                "threshold_quantity[]"
            )
            discounts = request.form.getlist(
                "discount_percent[]"
            )
            locked_tiers_raw = request.form.getlist(
                "locked_tier[]"
            )

            locked_tiers = []

            # hidden inputs kommen als "true" oder "false"
            # aus dem Formular zurück
            for value in locked_tiers_raw:
                if value == "true":
                    locked_tiers.append(True)
                else:
                    locked_tiers.append(False)

            # falls aus irgendeinem Grund ein hidden input fehlt,
            # ergänzen wir die Liste
            while len(locked_tiers) < len(thresholds):
                locked_tiers.append(False)

            # wenn der Nutzer nur eine weitere Zeile hinzufügen will,
            # speichern wir noch nicht
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

            try:
                min_participants_number = int(min_participants)
                base_price_number = float(base_price)
            except ValueError:
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
                    deadline=deadline,
                    error_message=(
                        "Mindestmenge und Basispreis müssen "
                        "gültige Zahlen sein."
                    )
                )

            if min_participants_number < 1:
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
                    deadline=deadline,
                    error_message=(
                        "Die Mindestmenge muss mindestens 1 betragen."
                    )
                )

            if base_price_number < 0:
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
                    deadline=deadline,
                    error_message=(
                        "Der Basispreis darf nicht negativ sein."
                    )
                )

            validation_error, validated_tiers = validate_tiers(
                thresholds,
                discounts
            )

            # bei ungültigen Rabattstaffeln bleibt der Nutzer
            # auf der Bearbeitungsseite
            if validation_error:
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
                    deadline=deadline,
                    error_message=validation_error
                )

            # hier speichern wir die normalen Hive-Daten
            update_hive(
                hive_id,
                title,
                game_system,
                short_description,
                description,
                deadline,
                min_participants_number,
                base_price_number
            )

            # die geprüften Rabattstaffeln werden
            # in getrennte Listen umgewandelt
            validated_thresholds = []
            validated_discounts = []

            for threshold, discount in validated_tiers:
                validated_thresholds.append(threshold)
                validated_discounts.append(discount)

            # hier ersetzen wir die Rabattstaffeln
            # durch die geprüften Werte aus dem Formular
            replace_hive_tiers(
                hive_id,
                validated_thresholds,
                validated_discounts
            )

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

        return render_template(
            "hive_buyers.html",
            hive=hive,
            buyers=buyers
        )