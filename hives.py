from flask import render_template, request, redirect, session, jsonify
from database import get_all_hives, get_hive_by_id, assign_hive_to_user, increase_hive_participants


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

        # hier geben wir den gefundenen Hive an die Detail-HTML-Datei weiter
        return render_template("hive_detail.html", hive=hive)


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