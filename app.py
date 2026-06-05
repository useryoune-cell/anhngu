from pathlib import Path

from flask import Flask, render_template, send_from_directory


BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/img/<path:filename>")
def image_asset(filename):
    return send_from_directory(BASE_DIR / "img", filename)


if __name__ == "__main__":
    app.run(debug=True)
