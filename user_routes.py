from flask import render_template


def setup_user_routes(app):
    # nutzer-routen sammeln

    @app.route("/register")
    def register():
        # registrierungsseite anzeigen
        return render_template("register.html")


    @app.route("/login")
    def login():
        # loginseite anzeigen
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