import unittest
import json
from app import create_app


class TestProduct(unittest.TestCase):

    def setUp(self):

        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        self.products = {
            "category":"kitchenware",
            "name":"pan"
        }
    def test_get_product(self):
        '''test get all products'''

        with self.client:
            response = self.client.get(
                '/api/v1/products',
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['Products'])

    def test_getSingleProduct(self):
        '''test get single product'''
        data = {"category":"electronics", "name":"TV"}
        with self.client:
            res = self.client.post('/api/v1/products', data = data)
            self.assertEqual(res.status_code, 201)
            response = self.client.get(
                '/api/v1/products/1',
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['response'])
