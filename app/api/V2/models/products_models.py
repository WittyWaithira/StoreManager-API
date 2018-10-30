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
        curr.execute("""SELECT id, category, name, price, quantity FROM products;""")
        data = curr.fetchall()
        resp = []
        for i, items in enumerate(data):
            id, name,category,quantity,price = items
            data = dict(
                products_id=int(id),
                name=name,
                category=category,
                quantity=int(quantity),
                price=int(price)
            )
            resp.append(data)
        return resp

    def fetchone(self, id):
        dbconn = self.con
        curr = dbconn.cursor()
        curr.execute("""SELECT id,category,name,price,quantity FROM products WHERE id = {};""".format(id))
        data = curr.fetchall()
        resp = []

        for i, items in enumerate(data):
            id,name,category,quantity,price = items
            data = dict(
                products_id_id=int(id),
                name = name,
                quantity=int(quantity),
                price=int(price)
            )
            resp.append(data)
        return resp


    def save(self, category, name,quantity,price):
        payload = {
              "category":category,
              "name":name,
              "quantity":quantity,
              "price":price
            }
        query = """INSERT INTO products (category,name,quantity,price) VALUES
                (%(category)s, %(name)s, %(quantity)s, %(price)s)"""
        curr = self.con.cursor()
        curr.execute(query, payload)
        self.con.commit()
        return payload

            # return "There is no such product"
