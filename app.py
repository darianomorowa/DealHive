from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "meine erste kleine Seite hehehe"


@app.route("/hives")
def hives_overview():
    return "hier werden hoffentlich bald Hives angezeigt!!!"


if __name__ == "__main__":
    app.run(debug=True)