from flask_restful import Resource
from flask import jsonify, make_response, request
from app.api.V2.models.products_models import ProductsData
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

class Products(Resource,ProductsData):
    def __init__(self):
        self.productsmodel = ProductsData()
    @jwt_required
    def get(self):
        result  = self.productsmodel.fetchall()
        return make_response(jsonify({
                "Products" : result
            }), 200)
    @jwt_required
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
    @jwt_required
    def get(self, productId):
        resp = self.productsmodel.fetchone(productId)

        return resp

class ModifyProduct(Resource):
    def __init__(self):
        self.productsmodel = ProductsData()
    @jwt_required
    def put(self,productId):
        data = request.get_json()
        if not data:
            return jsonify({"response": "Fields cannot be empty"})

        category = data['category']
        name = data['name']
        quantity = data['quantity']
        price = data ['price']

        resp = self.productsmodel.modify(category,name,quantity,price)
        return make_response(jsonify( {"Response" : resp, "message":"success"}), 201)

    def delete(self,id):
        resp = self.productsmodel.delete(id)
        return make_response(jsonify( {"Response" : resp, "message":"success"}), 200)
