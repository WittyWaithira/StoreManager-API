from app.db_config import init_db
from flask import make_response, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_raw_jwt

class User():
    def __init__(self):
        self.db = init_db()


    def save_user(self, email, name, password, role):
        user = {
            "email": email,
            "name":name,
            "password": password,
            "role": role
        }
        query = """INSERT INTO users (name, email, role, password) VALUES
                (%(name)s, %(email)s, %(role)s,  %(password)s)"""
        curr = self.db.cursor()
        curr.execute(query, user)
        self.db.commit()
        return user

    def login(self, email, password):
        """return user from the db given a username"""
        db = self.db
        curr = db.cursor()
        query = """SELECT *  FROM users WHERE email = '%s'""" % (email)
        response = curr.execute(query)
        data = curr.fetchone()

        dbpass = data[4]

        if (dbpass == password):
            #generate token
            token = create_access_token(identity=email)

            resp = make_response(jsonify(
                {
                    'Message' : 'Successful login',
                    'access_token' : token
                }), 200)

            return resp

        else:
            resp = make_response(jsonify(
                {
                    'Message' : 'Username and password does not match'
                }), 403)

            return resp
