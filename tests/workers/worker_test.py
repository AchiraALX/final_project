#!/usr/bin/env python3

"""Test for the workers module
"""

from workers.workers import _sum
import unittest
import requests


class WorkerTest(unittest.TestCase):
    """Test cases for the workers
    """

    api_home_uri = 'http://localhost:8000/'

    def test_sum(self):
        """Test sum, type, result"""

        _type = type(_sum(23, 23.3))
        total = _sum(23, 23.3)

        return self.assertTrue(total, 46.3) and self.assertTrue(_type, float)
