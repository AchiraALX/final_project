#!/usr/bin/env python3

"""Test for the structured database
"""

import unittest
from db.storage import Storage


class SQLTest(unittest.TestCase):
    """Testcase for the structured database
    """

    def test_connection(self):
        self.assertTrue(Storage('test'))
