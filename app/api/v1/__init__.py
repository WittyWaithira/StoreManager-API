from flask_restful import Api, Resource
from flask import Blueprint

#local imports goes here
from views import Sales, IndividualSales

version1  = Blueprint('api', __name__, url_prefix= '/api/v1')
api = Api(version1)

api.add_resource(Sales, '/sales')
api.add_resource(IndividualSales, '/sales/<int:id>')
