from flask import render_template, request, session
from database import create_user, get_user_by_username

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
            else:
                print("Login fehlgeschlagen")

        return render_template("login.html")

    @app.route("/profile")
    def profile():
        # profilseite anzeigen
        return render_template("profile.html")


    @app.route("/profile/edit")
    def edit_profile():
        # profil bearbeiten
        return render_template("edit_profile.html")


    @app.route("/logout")
    def logout():
        # logoutseite anzeigen
        return render_template("logout.html")