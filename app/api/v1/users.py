import re
from flask import request, jsonify
from flask_restful import Resource,reqparse
#from flask_jwt import JWT, jwt_required, current_identity
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_raw_jwt)
#from werkzeug.security import safe_str_cmp
from app.api.v1.models import user_models

users_list = user_models.Users()

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return jsonify({"message": "Email and password required"})

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"message": "Username or password missing"})

        authorize = users_list.verify_password(email, password)
        user=users_list.get_user_by_email(email)

        if authorize:
            access_token = create_access_token(identity=user)
            return jsonify(token = access_token, message = "Login successful!")

class UserRegistration(Resource):

    def post(self):
        data=request.get_json()
        name = data.get('name')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        role=data.get('role')

        roles=["owner","admin","attendant"]

        if role not in roles:
            return jsonify({"message":"The role {} does not exist".format(role)})

        email_format = re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

        if email_format is None:
            return jsonify({"message": "invalid email address"})

        response = jsonify(users_list.put(name, username, email, password,role))
        response.status_code = 201
        return response
