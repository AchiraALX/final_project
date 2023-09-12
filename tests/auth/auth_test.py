#!/usr/bin/env python3

"""Authentication tests
"""

from auth.t import ts
import unittest


class AuthTest(unittest.TestCase):
    """Test cases for authentication n sessions
    """

    def test_ts(self):
        self.assertEqual(ts(3, 2), 6)
