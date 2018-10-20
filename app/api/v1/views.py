from flask_restful import Resource
from flask import jsonify, make_response, request
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
from datetime import datetime
from flask.views import View

sales = []

product=[]

class Sales(Resource):


    def get(self):

        return make_response(jsonify({
            "Sales" : sales
        }), 200)

    def post(self):
        sales_data = request.get_json()

        # users data entered, stored in variables
        sales_id = sales_data['salesId']
        category = sales_data['category']
        sale_name = sales_data['product_name']
        quantity = sales_data['quantity']
        price = sales_data['price']

        # check if product is available in the products list
        for sale in sales:
            if sales_id==sale(["sales_id"]):
                return "{} already exists".format(sales_id),400
        # store products in a dictionary
        sales_cart = {
            "salesId":sales_id,
            "category":category,
            "product_name":sale_name,
            "quantity":quantity,
            "price":price
        }
        # add sale product to the sale list
        sales.append(sales_cart)

        # message to be displayed
        return jsonify({'response':'New Sale recorded'})


class SingleSales(Resource):
        def get(self, salesId):

            for sales in sale:
                if sales['salesId'] == salesId:
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
            product.append(users_products)

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
