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

class ProductsData():
    def __init__(self):
        #self.sale = sales
        self.product = product

    def fetchall(self):
        return self.product

    def fetchone(self, id):
        for product in self.product:
           if product['productId'] == id:
               return jsonify({"response": self.product})

               return jsonify({"response":"Product Not Available"})

    def save(self, category, name):
        #for product in self.product:
          #if product['name'] == name:
              #return "product already exists"

        for product in self.product:
             if product['name'] == name:
                 payload = {
                  "productId":len(self.product)+1,
                  "category":category,
                  "name":name
              }
             self.product.append(payload)
             return payload

             return "There is no such product"
