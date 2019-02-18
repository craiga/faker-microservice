"""Provider for Faker which adds fake microservice names."""

import faker.providers

SINGAULAR_NOUNS = [
    "aurora",
    "auth",
    "authentication",
    "authorisation",
    "azure",
    "bigquery",
    "cassandra",
    "cloud",
    "contact",
    "conversion",
    "cosmos",
    "database",
    "dynamo",
    "dynamodb",
    "elastic",
    "elasticsearch",
    "email",
    "error",
    "fraud",
    "fulfilment",
    "help",
    "legacy",
    "login",
    "maria",
    "memcache",
    "memcached",
    "mongo",
    "monolith",
    "mssql",
    "mysql",
    "oracle",
    "order",
    "payment",
    "postgres",
    "print",
    "promo",
    "promotion",
    "query",
    "rds",
    "redis",
    "redshift",
    "sale",
    "sms",
    "sql",
    "sqlite",
    "sqlserver",
    "user",
]

PLURAL_NOUNS = [
    "clouds",
    "contacts",
    "conversions",
    "databases",
    "emails",
    "errors",
    "logins",
    "orders",
    "payments",
    "promos",
    "promotions",
    "queries",
    "sales",
    "users",
]

DELIMITERS = ["", "-", "_"]

SUFFIXES = [
    "adapter",
    "adaptor",
    "api",
    "bridge",
    "data",
    "database",
    "db",
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
        """Simple microservice name (i.e. one without a suffix)"""
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
