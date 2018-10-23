import unittest
import json
from app import create_app


class TestProduct(unittest.TestCase):

    def setUp(self):

        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        self.products = {
            "productId":"123",
            "category":"kitchenware",
            "name":"pan"
        }
    def test_get_product(self):
        pass

    def test_getSingleProduct(self):
        pass
