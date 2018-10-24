import re
from flask_restful import Resource
from flask import jsonify, make_response, request
from app.api.v1.users_models import User,users

email_format = r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)"

user = User()

class UserLogin(Resource,User):
     def post(self):
        data = request.get_json()
        email = data["email"]
        password =data["password"]

        if not data:
            return jsonify("Fields cannot be empty")
        if not email or not password:
            return jsonify("You must provide username and password")

        if not re.match(email_format, email):
            return jsonify({"message": "Invalid Email address"})

        user_exists = [user for user in users if email == user["email"]]

        if not user_exists:
            return jsonify({
                "message":"User does not exist"
            })
        if password != user_exists[0]["password"]:
            return jsonify({
                "message":"Wrong password",
                "status": 400
            })

        access_token = create_access_token(identity=email)
        return jsonify(token = access_token, message = "Login successful!")

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
            return jsonify({"message":"You must provide email and password"})

        if not re.match(email_format, email):
            return jsonify({"message": "Invalid email address"})

        user_exists = [user for user in users if email == user["email"]]

        if user_exists:
            return jsonify({"message":"Email address already exists"})

        else:
            user.save_user(email,name, password, role)
            return jsonify({
                "message":"User has been registered successfully"
            })
