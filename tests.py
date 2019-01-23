"""Tests for faker-microservice."""

import unittest

from faker import Faker, Generator

import faker_microservice


class IntegrationTestCase(unittest.TestCase):
    """Integration tests."""

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(faker_microservice.Provider)

    def test_integration(self):
        """Test integration with Faker."""
        result = self.fake.microservice()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 1)

    def test_private_unavailable(self):
        """Test private method isn't available through Faker."""
        # pylint: disable=no-member,protected-access
        with self.assertRaises(AttributeError):
            self.fake._microservice_simple()
        with self.assertRaises(AttributeError):
            self.fake.microservice_simple()


class MicroserviceProviderTestCase(unittest.TestCase):
    """Provider test case."""

    # pylint: disable=protected-access

    def setUp(self):
        self.provider = faker_microservice.Provider(Generator())

    def test_simple(self):
        """Test simple microservice names."""
        result = self.provider._microservice_simple()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 1)

    def test_delimiter_and_suffix(self):
        """Test microservice names with delimiter and suffix."""
        result = self.provider._microservice_with_delimiter_and_suffix()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 1)

    def test_lists_in_order(self):
        """Test lists in root of module are in order."""
        for attr_name, attr in faker_microservice.__dict__.items():
            with self.subTest(attr_name=attr_name):
                if isinstance(attr, list):
                    self.assert_list_in_order(attr)

    def assert_list_in_order(self, the_list):
        """Assert a list is in order."""
        prev_value = ""
        for this_value in the_list:
            self.assertGreaterEqual(this_value, prev_value)
            prev_value = this_value


if __name__ == "__main__":
    unittest.main()
