#!/usr/bin/env python3

"""Call tests
"""
import unittest

from tests.workers.worker_test import WorkerTest
from tests.database.test_storage import SQLTest
from tests.api.api_test import APITest
from tests.auth.auth_test import AuthTest


def create_test_suite():
    """Create a test suite to run tests
    """

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # Add classes to th suite
    suite.addTest(loader.loadTestsFromTestCase(WorkerTest))
    suite.addTest(loader.loadTestsFromTestCase(SQLTest))
    suite.addTest(loader.loadTestsFromTestCase(APITest))
    suite.addTest(loader.loadTestsFromTestCase(AuthTest))

    return suite


class WTest(WorkerTest):
    """Tests for the workers

    Find the test file at /tests/workers/worker_test.py
    """

    def __str__(self) -> str:
        return "The worker tests"


class DBTests(SQLTest):
    """The tests for the structure query

    Find tests in /tests/database/test_storage.py
    """

    def __str__(self) -> str:
        return "These are test for the structured database"


class TestAPI(APITest):
    """Test case for the API

    Find the test file at /test/api/api_test.py
    """

    def __str__(self) -> str:
        return "These are the test for the API"


class TestAuth(AuthTest):
    """Test cases for the Authentication
    """

    def __str__(self) -> str:
        return "These are est cases for the Auth system"


if __name__ == "__main__":
    unittest.main(verbosity=2)
