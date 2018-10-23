from flask_restful import Resource
from flask import jsonify, make_response, request
from app.api.v1.models import SalesData
from app.api.v1.models import ProductsData


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
        category = data['category']
        name = data['name']

        resp = self.salesmodel.save(category, name)
        return jsonify( {"Response" : resp})


class SingleSales(Resource, SalesData):

    def __init__(self):
        self.salesmodel = SalesData()


    def get(self, salesId):
        """
            Get only a single sale using saleid
            param : Store Owner/admin and store attendant of the specific sale record
        """
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

        resp = self.productsmodel.save(category, name)
        return jsonify( {"Response" : resp})


class GetSingleProduct(Resource,ProductsData):
    def __init__(self):
        self.productsmodel = ProductsData()

    def get(self, productId):
        resp = self.productsmodel.fetchone(productId)

        return resp
