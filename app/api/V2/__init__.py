import os
from flask import Flask, Blueprint
from flask_restful import Api, Resource
from app.api.V2.views.sales_views import Sales,SingleSales
#from app.api.v1.views import Products,GetSingleProduct,TestMe
from app.api.V2.auth import Register
# from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

version2  = Blueprint('api2', __name__, url_prefix='/api/v2')
api = Api(version2)


api.add_resource(Sales, '/sales')
api.add_resource(SingleSales, '/sales/<int:salesId>')
#api.add_resource(Products, '/products')
#api.add_resource(GetSingleProduct, '/products/<int:productId>')
api.add_resource(Register, '/register')
#api.add_resource( UserLogin, '/login')
# test jwt function
#api.add_resource(TestMe, '/secret')
