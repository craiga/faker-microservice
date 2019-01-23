"""Provider for Faker which adds fake microservice names."""

import faker.providers

SINGAULAR_NOUNS = [
    "auth",
    "authentication",
    "authorisation",
    "cloud",
    "contact",
    "conversion",
    "email",
    "error",
    "fraud",
    "fulfilment",
    "help",
    "legacy",
    "login",
    "order",
    "payment",
    "print",
    "promo",
    "promotion",
    "sale",
    "sms",
    "user",
]

PLURAL_NOUNS = [
    "clouds",
    "contacts",
    "conversions",
    "emails",
    "errors",
    "logins",
    "orders",
    "payments",
    "promos",
    "promotions",
    "sales",
    "users",
]

DELIMITERS = ["", "-", "_"]

SUFFIXES = [
    "adapter",
    "adaptor",
    "api",
    "bridge",
    "interface",
    "manager",
    "platform",
    "processor",
    "service",
    "ui",
]


class Provider(faker.providers.BaseProvider):
    """Provider for Faker which adds fake microservice names."""

    def _microservice_simple(self):
        """'Simple' microservice name (i.e. one without a suffix)"""
        return self.random_element(SINGAULAR_NOUNS + PLURAL_NOUNS)

    def _microservice_with_delimiter_and_suffix(self):
        """Microservice name with delimiter and suffix."""
        return "".join(
            [
                self.random_element(SINGAULAR_NOUNS),
                self.random_element(DELIMITERS),
                self.random_element(SUFFIXES),
            ]
        )

    def microservice(self):
        """Fake microservice names."""
        return "".join(
            self.random_element(
                [
                    self._microservice_simple(),
                    self._microservice_with_delimiter_and_suffix(),
                ]
            )
        )
