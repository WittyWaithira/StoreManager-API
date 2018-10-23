from flask import Flask, Blueprint
#from instance.config import app_config


def create_app():
    app = Flask(__name__)
    from app.api.v1 import version1 as v1
    app.register_blueprint(v1)

    return app
