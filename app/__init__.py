import os
from flask import Flask, Blueprint
from flask_restful import Api
from instance.config import app_config
from flask_jwt_extended import JWTManager
#from app.api.v1 import version1 as v1
from app.db_config import create_tables, delete_tables
from app.api.V2 import version2 as V2


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    #delete_tables()
    create_tables()
    #app = Flask(__name__)
    # from app.api.v1 import version1 as v1

    #app.register_blueprint(v1)
    app.register_blueprint(V2)
    # app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    jwt = JWTManager(app)
    #app.config.from_object(app_config[config_name])
    #app.config.from_pyfile('config.py')

    return app
