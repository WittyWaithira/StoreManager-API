import unittest
import json
from app import create_app

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        self.register = {"email":"thuo254jerusha@gmail.com","password":"abe123A@","role":"admin","name":"jay"}
        self.register_user_invalid_email = { "email": "witty", "password":"jess345678","role":"admin","name":"jay" }
        self.register_user_empty_email = { "email": "", "password":"12345678", "role":"admin","name":"jay" }
        self.register_user_empty_password = { "email": "test@gmail.com", "password":"", "role":"admin","name":"jay" }
        self.login ={"email":"thuo254jerusha@gmail.com","password":"abe123A@"}
        self.login_user_empty_email= { "email": "", "password":"12345678" }
        self.login_user_empty_password= { "email": "jay@gmail.com", "password":"" }


    def test_post_register_success(self):
        response= self.client.post( '/api/v1/register',content_type='application/json',data=json.dumps(self.register))
        res= json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(res['message'], "User has been registred successfully")

    def test_post_register_invalid_email(self):
        response = self.client.post('/api/v1/register',content_type='application/json',data=json.dumps(self.register_user_invalid_email))
        res = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['message'], 'Invalid email address')

    def test_post_register_user_empty_email(self):
        response = self.client.post('/api/v1/register',content_type='application/json',data=json.dumps(self.register_user_empty_email))
        res= json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['message'], 'Blank email or password')

    def test_post_register_user_empty_password(self):
        response = self.client.post('/api/v1/register',content_type='application/json',data=json.dumps(self.register_user_empty_password))
        res = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['message'], 'Blank email or password')

    def test_post_login_success(self):
        response = self.client.post('/api/v1/login',content_type='application/json',data=json.dumps(self.login))
        res = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['message'], 'Login successful')

    def test_post_login_empty_email(self):
         response = self.client.post('/api/v1/login',content_type='application/json',data=json.dumps(self.login_user_empty_email))
         res = json.loads(response.data.decode('utf-8'))
         self.assertEqual(response.status_code, 400)
         self.assertEqual(res['message'], 'Fields cannot be empty')

    def test_post_login_empty_password(self):
        response = self.client.post('/api/v1/login',content_type='application/json',data=json.dumps(self.login_user_empty_password))
        res = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res['message'], 'Fields cannot be empty')
