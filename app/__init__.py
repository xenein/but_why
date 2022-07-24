import json

from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__)

    with open("./db_config.json") as fp:
        config = json.load(fp)

    app.config.update(config)

    @app.route("/")
    def start_view() -> str:
        return render_template("start.html")

    @app.route("/questions/")
    def questions_view() -> str:
        return render_template("questions.html")

    return app
