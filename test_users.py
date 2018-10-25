import unittest
import json
from app import create_app

class TestUsers(unittest.TestCase):

    def setUp(self):

        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        self.register = {
            "email":"thuo254jerusha@gmail.com",
            "password":"abe123A@",
            "role":"admin",
            "name":"jay"
        }
        self.login ={
            "email":"thuo254jerusha@gmail.com",
            "password":"abe123A@"
        }

    def test_post_register(self):
        response1 = self.client.post(
               '/api/v1/register',
                content_type='application/json',data=json.dumps(self.register)
           )
        res1 = json.loads(response1.data.decode('utf-8'))
        self.assertEqual(response1.status_code, 201)
        self.assertEqual(res1['message'], "User has been registered successfully")
        response = self.client.post(
               '/api/v1/register',
                content_type='application/json',data=json.dumps(self.register)
            )
        res = json.loads(response.data.decode('utf-8'))
        self.assertEqual(res['message'], "Email address already exists")




    def test_post_login(self):
        response = self.client.post(
               '/api/v1/register',
                content_type='application/json',data=json.dumps(self.register)
           )
        #self.assertEqual(response.status_code, 200)

        response = self.client.post(
               '/api/v1/login',
                content_type='application/json',data=json.dumps(self.login)
           )
        self.assertEqual(response.status_code,200)
