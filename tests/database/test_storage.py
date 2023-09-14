#!/usr/bin/env python3

"""Test for the structured database
"""

import unittest
from db.storage import Storage
from workers.workers import all_users


class SQLTest(unittest.TestCase):
    """Testcase for the structured database
    """

    storage = Storage('test')

    def test_connection(self):
        self.assertTrue(Storage('test'))

    def test_storage_get_user(self):
        """Test if the user can be retrieved correctly
        """

        self.assertTrue(all_users())
        self.assertEqual(type(all_users()), dict)
