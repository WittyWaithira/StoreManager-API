from flask_restful import Resource
from flask import jsonify, make_response, request

from .models import SalesOperattions

class Sales(Resource, SalesOperattions):

    def __init__(self):
        self.db = SalesOperattions()

    def get(self):
        result  = self.db.returnall()
        return make_response(jsonify({
            "Message" : "Success",
            "Sales" : result
        }), 200)

    def post(self):
        data = request.get_json()
        product = data['product']
        price = data['price']
        attendant = data['attendant']

        response = self.db.save(product, price, attendant)
        return make_response(jsonify({
            "Message" : "Success",
            "Sales" : response
        }), 201)


class SingleSales(Resource, SalesOperattions):

    def __init__(self):
        self.db = SalesOperattions()

    def get(self, id):
        result  = self.db.returnone(id)
        return make_response(jsonify({
            "Message" : "Success",
            "Sales" : result
        }))
