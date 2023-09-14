#!/usr/bin/env python3

"""Test for the structured database
"""

import unittest
from db.storage import Storage
from workers.workers import (
    all_users,
    all_blogs,
    get_user_by,
    get_blog_by,
    users_with_matching_query,
    blogs_with_matching_query,
    remove_user_self,
    remove_blog_self,
    update_user,
    update_blog
)
from db.models.user import User


class SQLTest(unittest.TestCase):
    """Testcase for the structured database
    """

    storage = Storage('test')

    def test_connection(self):
        self.assertTrue(Storage('test'))

    def test_storage_users(self):
        """Test if the user workers are working properly
        """

        self.assertTrue(all_users())
        self.assertEqual(type(all_users().__next__()), User)
        self.assertEqual(type(get_user_by(string='achira').__next__()), dict)

        self.assertEqual(get_user_by(string='achira').__next__(), {
            'id': '80bed6fb-254c-46bc-9c6c-02dfe8b6a235',
            'username': 'achira',
            'email': 'achi@gmail.com'
        })

    def test_storage_blog(self):
        """Test if blog workers are working properly
        """

        self.assertTrue(all_blogs())
