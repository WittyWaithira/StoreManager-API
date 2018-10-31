from flask import jsonify
from app.db_config import init_db

class ProductsData():
    def __init__(self):
         self.con = init_db()

    #def fetchall(self):
        #return self.product

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
        curr.execute("SELECT id,name,category,quantity,price FROM products WHERE id = '{}';".format(id))
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
        exist = self.check_product_exist(name)
        if exist == False:
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
        else:
            return "Product already exist"

    def modify(self, category, name,quantity,price):
        payload = {
             "category":category,
             "name":name,
              "quantity":quantity,
              "price":price
            }
        query = """UPDATE products SET category=%(category)s, name=%(name)s, quantity=%(quantity)s, price=%(price)s"""
        curr = self.con.cursor()
        curr.execute(query,payload)
        self.con.commit()
        return payload

    def delete(self,id):
        curr = self.con.cursor()
        query ="DELETE FROM products WHERE id='{}'".format(id)
        curr.execute(query)
        self.con.commit()
        return {"djjdj":"yes"},200

    def update_quantity_on_sales(self, name, quantity):
        dbconn = self.con
        curr = dbconn.cursor()
        query = "SELECT id, name, quantity, price FROM products WHERE name='{}'".format(name)
        curr.execute(query)
        data = curr.fetchone()
        if data:
            new_quantity = int(data[2]) - quantity
            curr.execute("UPDATE products SET quantity={} WHERE name='{}'".format(new_quantity, name))
            self.con.commit()
            return int(data[3])
        else:
            return False

    def check_product_exist(self, name):
        dbconn = self.con
        curr = dbconn.cursor()
        query = "SELECT name FROM products WHERE name='{}'".format(name)
        result = curr.execute(query)
        data = curr.fetchone()
        if data:
            return "Product already exists"
        else:
            return False
