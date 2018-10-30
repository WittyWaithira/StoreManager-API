from flask import jsonify
from app.db_config import init_db


class SalesData():
    def __init__(self):
         self.con = init_db()

    def fetchall(self):
        dbconn = self.con
        curr = dbconn.cursor()
        curr.execute("""SELECT id, items_sold, items, transaction_amount, date_created FROM sales;""")
        data = curr.fetchall()
        resp = []

        for i, items in enumerate(data):
            id, items_sold, items, transaction_amount, date_created = items
            data = dict(
                Sales_id=int(id),
                items=items,
                Quantity=int(items_sold),
                transaction_amount=int(transaction_amount),
                date=date_created
            )
            resp.append(data)
        return resp


    def fetchone(self, id):
        dbconn = self.con
        curr = dbconn.cursor()
        curr.execute("""SELECT id, items_sold, items, transaction_amount FROM sales WHERE id = {};""".format(id))
        data = curr.fetchall()
        resp = []

        for i, items in enumerate(data):
            id, items_sold,items, transaction_amount = items
            data = dict(
                Sales_id=int(id),
                items=items,
                Quantity=int(items_sold),
                transaction_amount=int(transaction_amount)
            )
            resp.append(data)
        return resp


    def save(self, items, items_sold,  transaction_amount):

        payload = {
            "items":items,
            "quantity":items_sold,
            "amount":transaction_amount
        }
        query = """INSERT INTO sales (items, items_sold, transaction_amount) VALUES
                (%(items)s, %(quantity)s, %(amount)s)"""
        curr = self.con.cursor()
        curr.execute(query, payload)
        self.con.commit()
        return payload

                # return "There is no such product"
