from flask_restful import Resource
from flask import jsonify, make_response, request
from app.api.v1.models import SalesData
from app.api.v1.models import ProductsData
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


class Sales(Resource, SalesData):

    def __init__(self):
        self.salesmodel = SalesData()

    def get(self):
        result  = self.salesmodel.fetchall()
        return make_response(jsonify({
            "Sales" : result
        }), 200)


    def post(self):
        data = request.get_json()
        if not data:
            return jsonify({"response": "Fields cannot be empty"})
        #id = data['salesId']
        items_sold = data['items']
        transaction_amount = data['amount']
        user_id = data['user']

        resp = self.salesmodel.save(items_sold, transaction_amount, user_id)
        return make_response(jsonify({
            "Response" : resp,
            "message":"Created successfully"
            }), 200)


class SingleSales(Resource, SalesData):

    def __init__(self):
        self.salesmodel = SalesData()


    def get(self, salesId):
        resp = self.salesmodel.fetchone(salesId)

        return resp




class Products(Resource):
    def __init__(self):
        self.productsmodel = ProductsData()

    def get(self):
        result  = self.productsmodel.fetchall()
        return make_response(jsonify({
                "Products" : result
            }), 200)

    def post(self):
        data = request.get_json()
        if not data:
            return jsonify({"response": "Fields cannot be empty"})

        category = data['category']
        name = data['name']
        quantity = data['quantity']
        price = data ['price']

        resp = self.productsmodel.save(category, name,quantity,price)
        return make_response(jsonify( {"Response" : resp, "message":"success"}), 201)


class GetSingleProduct(Resource,ProductsData):
    def __init__(self):
        self.productsmodel = ProductsData()

    def get(self, productId):
        resp = self.productsmodel.fetchone(productId)

        return resp

# test jwt
class TestMe(Resource):

    def get(self):
        current_user = 'me'
        access_token = create_access_token(identity = current_user)
        return {
            'answer': 42,
            'access_token': access_token
        }
