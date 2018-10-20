from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from instance.config import app_config
from app.api.v1 import version1

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.register_blueprint(version1)

    app.config['JWT_SECRET_KEY'] = 'thisismysecretkey'
    jwt = JWTManager(app)
    return app
