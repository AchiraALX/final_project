#!/usr/bin/env python3

"""Authentication tests
"""

from auth.t import ts
from auth.authenticate import Auth
import unittest


class AuthTest(unittest.TestCase):
    """Test cases for authentication n sessions
    """

    def test_ts(self):
        self.assertEqual(ts(3, 2), 6)

    def test_initiated(self):
        self.assertTrue(type(Auth(name='achira').initiated()), dict)
        self.assertEqual(Auth().initiated(), {})
        self.assertEqual(Auth(name='achira').initiated(), {'name': 'achira'})
        self.assertNotEqual(
            Auth(name='achira').initiated(), {})
