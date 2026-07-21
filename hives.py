from flask import render_template, request, redirect, session, jsonify
from database import (
    get_all_hives,
    get_hive_by_id,
    assign_hive_to_user,
    save_private_message,
    get_private_messages,
    get_hive_creator_id,
    get_user_by_id,
    can_users_chat_in_hive,
    get_connection,
    calculate_current_price,
    get_hive_tiers
)


def register_hive_routes(app):

    @app.route("/hives")
    def hives_overview():
        # Alle bestehenden Hives aus der Datenbank abrufen
        hives = get_all_hives()

        selected_game_system = request.args.get(
            "game_system",
            "all"
        )

        filtered_hives = []

        for hive in hives:
            if selected_game_system == "all":
                filtered_hives.append(hive)

            elif hive["game_system"] == selected_game_system:
                filtered_hives.append(hive)

        return render_template(
            "hives.html",
            hives=filtered_hives,
            selected_game_system=selected_game_system
        )

    @app.route("/hives/<int:hive_id>")
    def hive_detail(hive_id):
        hive = get_hive_by_id(hive_id)

        if hive is None:
            return "Hive wurde nicht gefunden."

        # Wir holen die ID des Erstellers,
        # damit der Button weiß, an wen der Chat geht
        creator_id = get_hive_creator_id(hive_id)

        # Nur Käufer dürfen einem fremden Hive beitreten
        can_join = (
            session.get("user_id") is not None
            and session.get("role") == "buyer"
            and session["user_id"] != creator_id
        )

        # Liveberechnung des Stückpreises
        # basierend auf Anzahl der Bestellungen
        current_price = calculate_current_price(hive_id)
        tiers = get_hive_tiers(hive_id)

        # hier geben wir den gefundenen Hive, den Creator,
        # den aktuellen Preis und die Rabattstufen
        # an die Detail-HTML-Datei weiter
        return render_template(
            "hive_detail.html",
            hive=hive,
            creator_id=creator_id,
            current_price=current_price,
            tiers=tiers,
            can_join=can_join
        )

    @app.route(
        "/hives/<int:hive_id>/join",
        methods=["POST"]
    )
    def join_hive(hive_id):
        # ohne Login soll niemand verbindlich
        # einem Hive beitreten
        if session.get("user_id") is None:
            return redirect("/login")

        # Nur in der Käufer-Ansicht darf
        # eine Bestellung abgeschlossen werden
        if session.get("role") != "buyer":
            return redirect(f"/hives/{hive_id}")

        hive = get_hive_by_id(hive_id)

        if hive is None:
            return "Hive wurde nicht gefunden.", 404

        # Der Creator darf seinem eigenen Hive
        # niemals als Käufer beitreten
        creator_id = get_hive_creator_id(hive_id)

        if creator_id == session["user_id"]:
            return redirect(f"/hives/{hive_id}")

        # hier lesen wir die gewünschte Stückmenge
        # aus dem Formular aus
        # wenn nichts mitkommt, nehmen wir als Standard
        # eine Stückzahl von 1
        try:
            quantity = int(
                request.form.get("quantity", 1)
            )
        except (TypeError, ValueError):
            return "Bitte gib eine gültige Stückzahl ein.", 400

        if quantity < 1:
            return "Du musst mindestens ein Stück bestellen.", 400

        # hier verbinden wir den eingeloggten Nutzer
        # mit dem Hive als Käufer
        # und übergeben die gewählte Stückzahl
        relation_was_created = assign_hive_to_user(
            session["user_id"],
            hive_id,
            "buyer",
            quantity=quantity
        )

        hive = get_hive_by_id(hive_id)

        return render_template(
            "join_confirm.html",
            hive=hive,
            relation_was_created=relation_was_created
        )

    # EBAY-UPDATE:
    # Die Chat-Route braucht jetzt zwingend die partner_id,
    # mit der man gerade schreibt
    @app.route(
        "/hives/<int:hive_id>/chat/<int:partner_id>",
        methods=["GET", "POST"]
    )
    def private_chat(hive_id, partner_id):
        if session.get("user_id") is None:
            return redirect("/login")

        current_user = session["user_id"]

        if request.method == "POST":
            message_text = request.form.get("message_text")

            if message_text:
                save_private_message(
                    hive_id,
                    current_user,
                    partner_id,
                    message_text
                )

            return redirect(
                f"/hives/{hive_id}/chat/{partner_id}"
            )

        hive = get_hive_by_id(hive_id)

        messages = get_private_messages(
            hive_id,
            current_user,
            partner_id
        )

        return render_template(
            "chat.html",
            hive=hive,
            messages=messages,
            partner_id=partner_id
        )

    @app.route("/my-chats")
    def my_chats():
        if session.get("user_id") is None:
            return redirect("/login")

        current_user = session["user_id"]

        connection = get_connection()

        user_chats = connection.execute("""
            SELECT DISTINCT
                hives.id AS hive_id,
                hives.title AS hive_title,
                CASE
                    WHEN messages.sender_id = ?
                    THEN messages.receiver_id
                    ELSE messages.sender_id
                END AS partner_id
            FROM messages
            JOIN hives ON messages.hive_id = hives.id
            WHERE messages.sender_id = ?
            OR messages.receiver_id = ?
        """, (
            current_user,
            current_user,
            current_user
        )).fetchall()

        connection.close()

        return render_template(
            "my_chats.html",
            chats=user_chats
        )

    @app.route("/api/hives")
    def api_hives():
        # Alle bestehenden Hives aus der Datenbank abrufen
        hives = get_all_hives()

        # leere Liste, in der wir die Hives
        # als Dictionary speichern
        hive_list = []

        # sqlite3.Row kann nicht direkt schön
        # als JSON ausgegeben werden
        # deshalb bauen wir jeden Hive
        # manuell als Dictionary um
        for hive in hives:
            hive_list.append({
                "id": hive["id"],
                "title": hive["title"],
                "game_system": hive["game_system"],
                "short_description": hive["short_description"],
                "deadline": hive["deadline"],
                "current_participants": hive[
                    "current_participants"
                ],
                "min_participants": hive["min_participants"]
            })

        # jsonify macht daraus
        # eine echte JSON-Antwort für die API
        return jsonify(hive_list)