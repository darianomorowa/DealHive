from flask import render_template, request, session, redirect
from database import (
    create_user,
    get_user_by_username,
    get_user_by_id,
    update_user_profile
)


def setup_user_routes(app):

    # nutzer-routen sammeln

    @app.route("/register", methods=["GET", "POST"])
    def register():

        if request.method == "POST":
            username = request.form["username"]
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            role = request.form["role"]
            street = request.form["street"]
            postal_code = request.form["postal_code"]
            city = request.form["city"]
            country = request.form["country"]

            create_user(
                username,
                name,
                email,
                password,
                role,
                street,
                postal_code,
                city,
                country
            )

            print("User gespeichert:", username)

            return redirect("/login")

        return render_template("register.html")


    @app.route("/login", methods=["GET", "POST"])
    def login():

        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]

            user = get_user_by_username(username)

            if user and user["password_hash"] == password:
                print("Login erfolgreich")

                session["user_id"] = user["id"]
                session["username"] = user["username"]
                session["role"] = user["role"]

                print(session["username"])

                return redirect("/profile")

            else:
                print("Login fehlgeschlagen")

        return render_template("login.html")


    @app.route("/profile")
    def profile():
        user_id = session.get("user_id")

        if user_id is None:
            return redirect("/login")

        user = get_user_by_id(user_id)

        return render_template(
            "profile.html",
            user=user
        )


    @app.route("/profile/edit", methods=["GET", "POST"])
    def edit_profile():
        user_id = session.get("user_id")

        if user_id is None:
            return redirect("/login")

        user = get_user_by_id(user_id)

        if request.method == "POST":
            name = request.form.get("name", "").strip()
            email = request.form.get("email", "").strip()
            role = request.form.get("role", "").strip()
            street = request.form.get("street", "").strip()
            postal_code = request.form.get("postal_code", "").strip()
            city = request.form.get("city", "").strip()
            country = request.form.get("country", "").strip()

            form_user = {
                "id": user_id,
                "name": name,
                "email": email,
                "role": role,
                "street": street,
                "postal_code": postal_code,
                "city": city,
                "country": country
            }

            # Alle Pflichtfelder prüfen
            if not all([
                name,
                email,
                role,
                street,
                postal_code,
                city,
                country
            ]):
                return render_template(
                    "edit_profile.html",
                    user=form_user,
                    error="Bitte fülle alle Pflichtfelder aus."
                )

            # Nur gültige Rollen erlauben
            if role not in ("buyer", "creator"):
                return render_template(
                    "edit_profile.html",
                    user=form_user,
                    error="Ungültige Rolle ausgewählt."
                )

            # Deutsche PLZ muss aus genau fünf Ziffern bestehen
            if not postal_code.isdigit() or len(postal_code) != 5:
                return render_template(
                    "edit_profile.html",
                    user=form_user,
                    error="Bitte gib eine gültige fünfstellige Postleitzahl ein."
                )

            update_user_profile(
                user_id,
                name,
                email,
                role,
                street,
                postal_code,
                city,
                country
            )

            session["role"] = role

            return redirect("/profile")

        return render_template(
            "edit_profile.html",
            user=user
        )


    @app.route("/logout")
    def logout():
        # session leeren, damit der Nutzer ausgeloggt ist
        session.clear()

        return redirect("/")
    

    @app.route("/session/role", methods=["POST"])
    def change_session_role():
        if session.get("user_id") is None:
            return redirect("/login")

        selected_role = request.form.get("role")

        if selected_role == "buyer" or selected_role == "creator":
            session["role"] = selected_role

        next_page = request.form.get("next_page", "/")

        return redirect(next_page)