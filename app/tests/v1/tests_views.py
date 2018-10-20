import sys
import json
import unittest

class TestProduct(unittest.TestCase):

    def setUp(self):
        # self.app = create_app(config_name="testing")
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        self.products = {
            "productId":"909",
            "category":"kitchenware",
            "name":"Dessini grill"
        }
