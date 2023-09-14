#!/usr/bin/env python3

"""General app tests
"""


import requests
from unittest import TestCase


class ChatTest(TestCase):
    """Test class for the general chat routes
    """

    chat_home_uri = 'http://localhost:8000/'

    def test_get_registration_form(self):
        """Test getting the registration form
        """

        code = requests.get(self.chat_home_uri).status_code

        self.assertEqual(code, 200)
