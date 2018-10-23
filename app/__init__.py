from flask import Flask, Blueprint
from flask_restful import Api
from instance.config import app_config


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    #app = Flask(__name__)
    from app.api.v1 import version1 as v1

    app.register_blueprint(v1)
    #app.config.from_object(app_config[config_name])
    #app.config.from_pyfile('config.py')

    return app
