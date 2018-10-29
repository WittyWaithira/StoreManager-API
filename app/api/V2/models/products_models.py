from flask import jsonify
from app.db_config import init_db

class ProductsData():
    def __init__(self):
         self.con = init_db()

    def fetchall(self):
        return self.product

    def fetchall(self):
        dbconn = self.con
        curr = dbconn.cursor()
        curr.execute("""SELECT id, name,category ,quantity, price,sales_id FROM products;""")
        data = curr.fetchall()
        resp = []
        for i, items in enumerate(data):
            id, name,category,quantity,price,sales_id = items
            data = dict(
                products_id=int(id),
                category=category,
                quantity=int(quantity),
                transaction_amount=int(transaction_amount),
                date=date_created
            )
            resp.append(data)
        return resp


    def save(self, category, name,quantity,price,sales_id):
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
