#!/usr/bin/env python3

"""API tests
"""

import unittest
from api.api import api
import requests
from app.main import chat


class APITest(unittest.TestCase):
    """Tests for the application interface
    """
    api_home_uri = 'http://localhost:8000/'

    def test_api_home(self):
        """Test the home page
        """

        self.assertEqual(requests.get(self.api_home_uri).status_code, 200)

    async def test_api_get_users(self):
        """Test for the getting users route
        """

        response = await chat.test_client().get('/users/test')

        self.assertEqual(requests.get(
            self.api_home_uri + 'get_users').status_code, 200)
