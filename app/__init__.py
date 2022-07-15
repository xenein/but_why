import json

from flask import Flask


def create_app():
    app = Flask(__name__)

    with open("./db_config.json") as fp:
        config = json.load(fp)

    app.config.update(config)

    return app
