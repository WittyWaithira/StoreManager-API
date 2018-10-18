from flask_restful import Resource
from flask import jsonify, make_response, request
from datetime import datetime

sales = []


class Sales(Resource):


    def get(self):
        return jsonify(sales)
        return make_response(jsonify({
            "Message" : "Success",
            "Sales" : result
        }), 200)

    def post(self):
        data = request.get_json()
        if not data:
            return jsonify({"message":"You cannot leave this empty"})

            sales_id : len(sales)+1
            product : 'product'
            price: 'price'
            attendant : 'attendant'
            time : datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

        if not product or product == " ":
            return jsonify({"message": "Please enter product name"}), 404
        else:
            payload = {
			'sale_id':sale_id,
			'product': product,
            'price':price,
			'attendant': attendant
			}
        sales.append(payload)
        return make_response(jsonify({'list': sales}))


class SingleSales(Resource):
    def get(self, id):
        sale = [sale for sale in sales if sale['sale_id'] == sale_id] or None
        if sale:
            return jsonify({'sale':sale[0]})
        else:
            return jsonify({'message': "item not found"})
            return 404
