from flask import Flask, render_template
from database import create_tables
from creator_routes import register_creator_routes
from user_routes import setup_user_routes
from hives import register_hive_routes

#Zugriff auf unsere Projektbilder ermöglichen
app = Flask(__name__, static_folder="docs/assets", static_url_path="/assets")

# secret_key brauchen wir, damit Flask Sessions speichern kann
# da wir nur mit Testdaten arbeiten kann auf komplexe Sicherheit vorerst verzichtet werden
app.secret_key = "dealhive-dev-secret-key"

# Datenbanktabellen beim Start der App initialisieren
create_tables()

# hier registrieren wir die Creator-Routen aus creator_routes.py
register_creator_routes(app)

# nutzer-routen laden
setup_user_routes(app)

# hier registrieren wir die Hive-Routen aus hives.py
register_hive_routes(app)


@app.route("/")
def home():
    # hier landet der Nutzer auf der Startseite
    # nach Login oder Registrierung leiten wir später auch hierhin zurück
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)