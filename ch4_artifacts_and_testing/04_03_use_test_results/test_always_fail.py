"""Intentional failing tests for CI/CD pipeline demonstrations"""

import unittest


class TestIntentionalFailures(unittest.TestCase):
    """
    These tests are designed to fail.
    They are used to demonstrate how pipelines respond to test failures.
    """

    def test_ALWAYS_FAIL_1(self):
        """This test always fails on purpose"""
        self.fail("Intentional failure for pipeline demonstration")

    def test_ALWAYS_FAIL_2(self):
        """test_ALWAYS_FAIL: this test will always fail"""
        assert False
