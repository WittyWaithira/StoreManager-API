from flask_restful import Resource
from flask import jsonify, make_response, request
#from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
#from datetime import datetime
from flask.views import View

sales = []

products=[]

class Sales(Resource):

    def get(self):
        return make_response(jsonify({
            "Sales" : sales
        }), 200)


    def post(self):
        data = request.get_json()
        if not data:
            return jsonify({"response": "Fields cannot be empty"})
        id = data['salesId']
        category = data['category']
        name = data['name']

        # dictionary data structure for users products
        sales_record = {
            "salesId":id,
            "category":category,
            "name":name
        }
        # Store products obtained from the user in a list
        sales.append(sales_record)

        # message to be displayed to the user
        return jsonify( {'response':'New product added successfully'})


class SingleSales(Resource):
    def get(self, salesId):
        """
            Get only a single sale using saleid
            param : Store Owner/admin and store attendant of the specific sale record
        """
        for sale in sales:
            if sale['salesId'] == salesId:
                return jsonify({"response":sales})

        return jsonify({"response":"Product Not Available"})



class Products(Resource):

        def get(self):

            return make_response(jsonify(
                {
                    'Products':product
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
