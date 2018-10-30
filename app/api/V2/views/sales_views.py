from flask_restful import Resource
from flask import jsonify, make_response, request
from app.api.V2.models.sales_models import SalesData
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


class Sales(Resource, SalesData):

    def __init__(self):
        self.salesmodel = SalesData()
    @jwt_required
    def get(self):
        result  = self.salesmodel.fetchall()
        return make_response(jsonify({
            "Sales" : result
        }), 200)

    @jwt_required
    def post(self):
        data = request.get_json()
        if not data:
            return jsonify({"response": "Fields cannot be empty"})
        items = data['items']
        items_sold = data['quantity']
        transaction_amount = data['amount']
        user_id = data['user']

        resp = self.salesmodel.save(items, items_sold, transaction_amount)
        return make_response(jsonify({
            "Response" : resp,
            "message":"Created successfully"
            }), 200)


class SingleSales(Resource, SalesData):

    def __init__(self):
        self.salesmodel = SalesData()

    @jwt_required
    def get(self, salesId):
        resp = self.salesmodel.fetchone(salesId)

        return resp
