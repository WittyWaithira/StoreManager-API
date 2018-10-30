import re
from flask_restful import Resource
from flask import jsonify, make_response, request
from app.api.V2.models.users_models import User

email_format = r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)"



class UserLogin(Resource, User):
    def __init__(self):
        self.user = User()

    def post(self):
        data = request.get_json()
        email = data["email"]
        password =data["password"]

        if not data:
            return {'message': 'Data should be in json format'}, 400

        if not email or not password:
            return {'message': 'Fields cannot be empty'}, 400 #400 bad request


        if not re.match(email_format, email):
            return {'message': 'Invalid email address'}, 400

        resp = self.user.login(email, password)
        return resp

class Register(Resource, User):
    def __init__(self):
        self.user = User()

    def post(self):
        data = request.get_json()

        email = data["email"]
        password = data["password"]
        role = data["role"]
        name = data["name"]

        if not data:
            return jsonify("Data must be in json format")
        if not email or not password:
            return {'message': 'Blank email or password'}, 400

        if not re.match(email_format, email):
            return {'message': 'Invalid email address'}, 400

        else:
            resp = self.user.save_user(email, name, password, role)
            return make_response(jsonify({
                'message': 'User has been registred successfully'
            }),201)
