from flask import render_template, request, session, redirect
from database import create_user, get_user_by_username, get_user_by_id


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


    @app.route("/profile/edit")
    def edit_profile():
        # profil bearbeiten
        return render_template("edit_profile.html")


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