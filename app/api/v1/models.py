from flask import jsonify

sales = []
product = []

class SalesData():
    def __init__(self):
         self.sale = sales
         self.product = product

    def fetchall(self):
        return self.sale


    def fetchone(self, id):
        for sale in self.sale:
            if sale['salesId'] == id:
                return jsonify({"response": self.sale})

        return jsonify({"response":"Product Not Available"})


    def save(self, category, name):
        for sale in self.sale:
            if sale['name'] == name:
                return "product already exists"

        for product in self.product:
            if product['name'] == name:
                payload = {
                    "salesId":len(self.sale)+1,
                    "category":category,
                    "name":name
                }
                self.sale.append(payload)
                return payload

        return "There is no such product"
