"""
Unit tests for DataProcessor.
"""

import unittest

from data_processor import DataProcessor


class TestDataProcessor(unittest.TestCase):
    """Test cases for DataProcessor class."""

    def setUp(self):
        """Set up test fixtures."""
        self.processor = DataProcessor()

    def test_get_user_info_success(self):
        """Test that get_user_info works correctly."""
        result = self.processor.get_user_info()
        self.assertEqual(result, "John Doe")

    def test_get_incomplete_data(self):
        """
        Test that demonstrates accessing incomplete data.
        """
        result = self.processor.get_incomplete_data()
        self.assertIsNotNone(result)

    def test_get_empty_list(self):
        """
        Test that demonstrates accessing an empty list.
        """
        result = self.processor.get_empty_list()
        self.assertIsNotNone(result)

    def test_get_malformed_structure(self):
        """
        Test that demonstrates malformed data structure access.
        """
        result = self.processor.get_malformed_structure()
        self.assertIsNotNone(result)

    def test_process_safely(self):
        """Test the non-wrapped method."""
        result = self.processor.process_safely("user")
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
