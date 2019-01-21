"""Tests for faker-microservice."""

import unittest

from faker import Faker

from faker_microservice import MicroserviceProvider


class IntegrationTestCase(unittest.TestCase):
    """Integration tests."""

    def test_integration(self):  # pylint: disable=no-self-use
        """Test integration with Faker."""
        fake = Faker()
        fake.add_provider(MicroserviceProvider)
        fake.microservice()


if __name__ == "__main__":
    unittest.main()
