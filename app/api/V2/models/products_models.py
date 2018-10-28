from flask import jsonify
from app.db_config import init_db


class SalesData():
    def __init__(self):
         self.con = init_db()

    def fetchall(self):
        dbconn = self.con
        curr = dbconn.cursor()
        curr.execute("""SELECT id, items_sold, transaction_amount, date_created, user_id FROM sales;""")
        data = curr.fetchall()
        resp = []

        for i, items in enumerate(data):
            id, items_sold, transaction_amount, date_created, user_id = items
            data = dict(
                Sales_id=int(id),
                user=user_id,
                items_sold=items_sold,
                transaction_amount=int(transaction_amount),
                date=date_created
            )
            resp.append(data)
        return resp


    def fetchone(self, id):
        for sale in self.sale:
            if sale['salesId'] == id:
                return jsonify({"response": sale})

        return jsonify({"response":"Product Not Available"})


    def save(self, items_sold, transaction_amount, user_id):

        payload = {
            "items":items_sold,
            "amount":transaction_amount,
            "user":user_id
        }
        query = """INSERT INTO sales (items_sold, transaction_amount, user_id) VALUES
                (%(items)s, %(amount)s, %(user)s)"""
        curr = self.db.cursor()
        curr.execute(query, payload)
        self.db.commit()
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
