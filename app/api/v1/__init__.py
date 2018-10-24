from flask import Flask, Blueprint
from flask_restful import Api, Resource
from app.api.v1.views import Sales,SingleSales
from app.api.v1.views import Products,GetSingleProduct
from app.api.v1.users import Register,UserLogin

version1  = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)


api.add_resource(Sales, '/sales')
api.add_resource(SingleSales, '/sales/<int:salesId>')
api.add_resource(Products, '/products')
api.add_resource(GetSingleProduct, '/products/<int:productId>')
api.add_resource(Register, '/register')
api.add_resource( UserLogin, '/login')
