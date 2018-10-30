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
                return jsonify({"response": sale})

        return jsonify({"response":"Product Not Available"})


    def save(self, category, name,quantity,price):
        for sale in self.sale:
            if sale['name'] == name:
                return "sale already exists"

        payload = {
            "salesId":len(self.sale)+1,
            "category":category,
            "name":name,
            "quantity":quantity,
            "price":price
        }
        self.sale.append(payload)
        return payload

                # return "There is no such product"

class ProductsData():
    def __init__(self):
        #self.sale = sales
        self.product = product

    def fetchall(self):
        return self.product

    def fetchone(self, id):
        for product in self.product:
            if product['productId'] == id:
                return jsonify({"response": product})

        return jsonify({"response":"Product Not Available"})

    def save(self, category, name,quantity,price):
        for product in self.product:
            if product['name'] == name:
                return "Product exists"
        payload = {
              "productId":len(self.product)+1,
              "category":category,
              "name":name,
              "quantity":quantity,
              "price" :price
            }
        self.product.append(payload)
        return payload

            # return "There is no such product"
