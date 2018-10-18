from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api, reqparse

#from app.api.models import products

products = []

class Products(Resource):

	def get(self):

		return jsonify(products)
		return jsonify({'message':'Item not found'},
						{'status': 200}
			)





	def post(name):
		
		data = request.get_json()
		if not data:
			return jsonify({"message": "field cannot be empty"})
		name = data['name']
		price = data['price']
		product_id = len(products)+1
		quantity = data['quantity']
		if not name or name == "":
			return jsonify({"message": "Please enter product name"}), 404
		else:

			payload = {
			'name': name,
			'price': price,
			'product_id': product_id,
			'quantity': quantity
			}

			products.append(payload)

			return make_response(jsonify({'list': products}), 201)



class Product_id(Resource):

	def get(self, product_id):
		product = [product for product in products if product['product_id'] == product_id] or None
		if product:
			return jsonify({'product':product[0]})
		else:
			return jsonify({'message': "specific product not found"})
		return 404
