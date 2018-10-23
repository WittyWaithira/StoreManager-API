from flask_restful import Resource
from flask import jsonify, make_response, request
#from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
#from datetime import datetime
#from flask.views import View
from app.api.v1.models import SalesData


products=[]

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

        def get(self):

            return make_response(jsonify(
                {
                    'Products':products
                }
            ),200)


        def post(self):

            # fetch users input data
            data = request.get_json()
            if not data:
                return jsonify({"response": "Fields cannot be empty"})
            id = data['productId']
            category = data['category']
            name = data['name']

            # dictionary data structure for users products
            users_products = {
                "productId":id,
                "category":category,
                "name":name
            }
            # Store products obtained from the user in a list
            products.append(users_products)

            # message to be displayed to the user
            return jsonify( {'response':'New product added successfully'})

class GetSingleProduct(Resource):
    ''' fetch a single product '''

    def get(self, productId):
            """Fetch a single product record
                param:
                <int:productId>
            """
            for product in products:
                if product['productId'] == productId:
                    return jsonify(
                        {
                            'response':product
                        }
                    )
            return jsonify({'response':'Product Not Available'})
