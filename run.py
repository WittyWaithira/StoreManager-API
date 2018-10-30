import os
from app import create_app
# from flask_jwt_extended import JWTManager


app = create_app()
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True)
