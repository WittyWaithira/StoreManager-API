import unittest
import json
from app import create_app


class TestSales(unittest.TestCase):

    def setUp(self):

        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        self.products = {
            "category":"kitchenware",
            "name":"pan"
        }
    def test_get_sale(self):
        '''test get all sales'''
        with self.client:
            response = self.client.get(
                '/api/v1/sales',
                content_type='application/json'
            )
            result = json.loads(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 200, result['Sales'])

        

    def test_get_single_sale(self):
        '''test get single sale'''

        with self.client:
            response = self.client.post('/api/v1/sales', data=json.dumps(self.products),content_type='application/json')
            self.assertEqual(response.status_code, 200)
