import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db, login_manager
from application.models import Users
from flask_login import login_user, logout_user




class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        app.config.update(
            SQLALCHEMY_DATABASE_URI=getenv('LOGIN_DB_URI'),
            SECRET_KEY=getenv('SECRET_KEY'),
            WTF_CSRF_ENABLED=False,
            DEBUG=True
        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        user = Users.query.first()

    def tearDown(self):
        """
        Will be called after every test
        """
        user = Users.query.first()

class TestLoginFunc(TestBase):
    def test_login_view(self):
        response = self.client.get(
            '/login'
        )
        self.assertEqual(response.status_code, 200)

    def test_wrong_password(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(
                    email="test@email.com",
                    password="password123"
                ),
                follow_redirects=True
            )
            self.assertIn(b'Incorrect Email or Password', response.data)

    def test_successful_login(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(
                    email="test@email.com",
                    password="password"
                ),
                follow_redirects=True
            )
            self.assertIn(b'You are logged in', response.data)



if __name__ == '__main__':
    unittest.main()