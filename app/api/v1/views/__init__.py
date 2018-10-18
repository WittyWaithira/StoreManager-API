from flask_restful import Api, Resource
from flask import Blueprint

#local imports goes here
from views.products import Products, Product_id
from  views.sales import Sales,SingleSales

version1  = Blueprint('api', __name__, url_prefix= '/api/v1')
api = Api(version1)

api.add_resource(Sales, '/sales')
api.add_resource(SingleSales, '/sales/<int:id>')
api.add_resource(Products, '/products')
api.add_resource(Product_id, '/products/<int:product_id>')
