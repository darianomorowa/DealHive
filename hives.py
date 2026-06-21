from flask import render_template, request, redirect, session, jsonify
from database import (
    get_all_hives,
    get_hive_by_id,
    assign_hive_to_user,
    increase_hive_participants,
    save_private_message,
    get_private_messages,
    get_hive_creator_id,
    get_connection,
    calculate_current_price,
    get_hive_tiers
)

def register_hive_routes(app):

    @app.route("/hives")
    def hives_overview():
        # Alle bestehenden Hives aus der Datenbank abrufen
        hives = get_all_hives()

        # variable für "welches System" - Filter
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


    # Detailroute
    @app.route("/hives/<int:hive_id>")
    def hive_detail(hive_id):
        # Spezifischen Hive anhand der ID aus der Datenbank auslesen
        hive = get_hive_by_id(hive_id)

        # Fehlerbehandlung: Falls die ID nicht existiert
        if hive is None:
            return "Hive wurde nicht gefunden."

       # Wir holen die ID des Erstellers, damit der Button weiß, an wen der Chat geht
        creator_id = get_hive_creator_id(hive_id)

    # Liveberechnung Stückpreises basierend auf anzahl der Bestellungen
        current_price = calculate_current_price(hive_id)
        tiers = get_hive_tiers(hive_id)

        # hier geben wir den gefundenen Hive (und den Creator) an die Detail-HTML-Datei weiter und Preise + Rabattstufen
        return render_template("hive_detail.html", hive=hive, creator_id=creator_id, current_price=current_price, tiers=tiers)


    @app.route("/hives/<int:hive_id>/join", methods=["POST"])
    def join_hive(hive_id):
         # ohne Login soll niemand verbindlich einem Hive beitreten
        if session.get("user_id") is None:
            return redirect("/login")

    # hier verbinden wir den eingeloggten Nutzer mit dem Hive als Käufer
        relation_was_created = assign_hive_to_user(session["user_id"], hive_id, "buyer")

    # die Teilnehmerzahl wird nur erhöht, wenn der Beitritt neu war
        if relation_was_created:
            increase_hive_participants(hive_id)

    # hier zeigen wir die Bestätigungsseite nach dem Beitritt
        return render_template("join_confirm.html")


    # EBAY-UPDATE: Die Chat-Route braucht jetzt zwingend die partner_id, mit der man gerade schreibt
    @app.route("/hives/<int:hive_id>/chat/<int:partner_id>", methods=["GET", "POST"])
    def private_chat(hive_id, partner_id):
        # Sicherheits-Check: Nur eingeloggte User dürfen chatten
        if session.get("user_id") is None:
            return redirect("/login")

        current_user = session["user_id"]

        # Wenn der User eine Nachricht absendet (POST)
        if request.method == "POST":
            message_text = request.form.get("message_text")
            
            if message_text:
                # Nachricht wird gezielt an die partner_id geschickt
                save_private_message(hive_id, current_user, partner_id, message_text)
            
            # Seite neu laden, um die Nachricht sofort zu sehen
            return redirect(f"/hives/{hive_id}/chat/{partner_id}")

        # Wenn die Seite normal aufgerufen wird (GET)
        hive = get_hive_by_id(hive_id)
        # Wir laden nur Nachrichten zwischen dir und exakt diesem Partner
        messages = get_private_messages(hive_id, current_user, partner_id)

        return render_template("chat.html", hive=hive, messages=messages, partner_id=partner_id)
    
    
    # EBAY-UPDATE: Der globale Posteingang
    @app.route("/my-chats")
    def my_chats():
        # Sicherheits-Check: Nur für eingeloggte User
        if session.get("user_id") is None:
            return redirect("/login")
        
        current_user = session["user_id"]
        
        # Wir suchen alle aktiven Chats für diesen User aus der Tabelle (wer hat mit wem geschrieben)
        connection = get_connection()
        user_chats = connection.execute("""
            SELECT DISTINCT 
                hives.id AS hive_id, 
                hives.title AS hive_title,
                CASE 
                    WHEN messages.sender_id = ? THEN messages.receiver_id 
                    ELSE messages.sender_id 
                END AS partner_id
            FROM messages
            JOIN hives ON messages.hive_id = hives.id
            WHERE messages.sender_id = ? OR messages.receiver_id = ?
        """, (current_user, current_user, current_user)).fetchall()
        connection.close()
        
        # Übergabe der Chat-Liste an das Template
        return render_template("my_chats.html", chats=user_chats)


    @app.route("/api/hives")
    def api_hives():
        # Alle bestehenden Hives aus der Datenbank abrufen
        hives = get_all_hives()

        # leere Liste, in der wir die Hives als Dictionary speichern
        hive_list = []

        # sqlite3.Row kann nicht direkt schön als JSON ausgegeben werden
        # deshalb bauen wir jeden Hive manuell als Dictionary um
        for hive in hives:
            hive_list.append({
                "id": hive["id"],
                "title": hive["title"],
                "game_system": hive["game_system"],
                "short_description": hive["short_description"],
                "deadline": hive["deadline"],
                "current_participants": hive["current_participants"],
                "min_participants": hive["min_participants"]
            })

        # jsonify macht daraus eine echte JSON-Antwort für die API
        return jsonify(hive_list)