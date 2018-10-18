from datetime import datetime

sales = []

class SalesOperattions():

    def __init__(self):
        self.db = sales

    def save(self, product, price, attendant):
        payload = {
            "sales_id" : len(self.db)+1,
            "product" : product,
            "price" : price,
            "attendant" : attendant,
            "time" : datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
        }

        self.db.append(payload)
        return payload

    def returnall(self):
        return self.db

    def returnone(self, id):
        for sale in self.db:
            if (id == sale['sales_id']):
                return sale, 200

        return "Sales with that id not found", 404
