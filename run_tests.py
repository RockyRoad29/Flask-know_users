# -*- coding: utf-8 -*-
"""
    Tests
    ~~~~~

    Tests the KnowUsers app
"""
import unittest
from playground import app
from playground.example.models import db, Member


class KnowUsersTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_urls(self):
        r = self.app.get('/')
        self.assertEquals(r.status_code, 200)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were successfully logged in' in rv.data
        rv = self.logout()
        assert 'You were successfully logged out' in rv.data
        rv = self.login('adminx', 'default')
        assert 'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in rv.data

if __name__ == '__main__':
    unittest.main()
