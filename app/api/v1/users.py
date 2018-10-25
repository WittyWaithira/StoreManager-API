import re
from flask_restful import Resource
from flask import jsonify, make_response, request
#from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_raw_jwt
from app.api.v1.users_models import User,users

email_format = r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)"

user = User()

class UserLogin(Resource,User):
     def post(self):
        data = request.get_json()
        email = data["email"]
        password =data["password"]

        if not data:
            return {'message': 'Fields cannot be empty'}, 400

        if not email or not password:
            return {'message': 'Fields cannot be empty'}, 400 #400 bad request


        if not re.match(email_format, email):
            return {'message': 'Invalid email address'}, 400


        user_exists = [user for user in users if email == user["email"]]

        if not user_exists:
            return {'message': 'User does not exist'}, 400
        if password != user_exists[0]["password"]:
            return {'message': 'Wrong password'}, 400

        # access_token = create_access_token(identity=email)
        # return jsonify(token = access_token, message = "Login successful!")
        return {'message': 'Login successful'}, 200

class Register(Resource, User):

    def post(self):
        data = request.get_json()

        email = data["email"]
        password =data["password"]
        role = data["role"]
        name = data["name"]

        if not data:
            return jsonify("Data must be in json format")
        if not email or not password:
            return {'message': 'Invalid email or password'}, 400

        if not re.match(email_format, email):
            return {'message': 'Invalid email address'}, 400

        user_exists = [user for user in users if email == user["email"]]

        if user_exists:
            return {'message': 'Email address already exists'}, 400


        else:
            user.save_user(email,name, password, role)
            return {'message': 'User has been registred successfully'}, 200
