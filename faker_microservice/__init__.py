"""Provider for Faker which adds fake microservice names."""

import random

import faker.providers

SINGULAR_NOUNS = [
    "aurora",
    "auth",
    "authentication",
    "authorisation",
    "azure",
    "bigquery",
    "blob",
    "blog",
    "cassandra",
    "cloud",
    "contact",
    "conversion",
    "cosmos",
    "database",
    "document",
    "dynamo",
    "dynamodb",
    "elastic",
    "elasticsearch",
    "email",
    "error",
    "fraud",
    "ftp",
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
    "sftp",
    "smb",
    "sms",
    "smtp",
    "sql",
    "sqlite",
    "sqlserver",
    "user",
]

PLURAL_NOUNS = [
    "blogs",
    "clouds",
    "contacts",
    "conversions",
    "databases",
    "documents",
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

PREFIXES = ["legacy", "new", "old"]


SUFFIXES = [
    "adapter",
    "adaptor",
    "api",
    "backend",
    "be",
    "bridge",
    "dashboard",
    "data",
    "database",
    "db",
    "fe",
    "frontend",
    "interface",
    "manager",
    "platform",
    "processor",
    "service",
    "ui",
]


class Provider(faker.providers.BaseProvider):
    """Provider for Faker which adds fake microservice names."""

    def microservice(self):
        """Fake microservice names."""
        delimiter = self.random_element(DELIMITERS)
        prefix = self.random_element(PREFIXES)
        suffix = self.random_element(SUFFIXES)
        noun = self.random_element(SINGULAR_NOUNS + PLURAL_NOUNS)
        singular_noun = self.random_element(SINGULAR_NOUNS)

        delimiters_weight = 1
        prefixes_weight = 1
        suffixes_weight = len(SUFFIXES)
        nouns_weight = len(SINGULAR_NOUNS + PLURAL_NOUNS)
        singular_nouns_weight = len(SINGULAR_NOUNS)

        choices = [
            noun,
            "".join([singular_noun, delimiter, suffix]),
            "".join([prefix, delimiter, singular_noun]),
            "".join([prefix, delimiter, singular_noun, delimiter, suffix]),
        ]
        weights = [
            nouns_weight,
            singular_nouns_weight * delimiters_weight * suffixes_weight,
            prefixes_weight * delimiters_weight * singular_nouns_weight,
            prefixes_weight
            * delimiters_weight
            * singular_nouns_weight
            * delimiters_weight
            * suffixes_weight,
        ]

        names = random.choices(choices, weights=weights, k=1)

        return names[0]
