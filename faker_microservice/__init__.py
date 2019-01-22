"""Provider for Faker which adds fake microservice names."""

import faker.providers


class Provider(faker.providers.BaseProvider):
    """Provider for Faker which adds fake microservice names."""

    def microservice(self):
        """Fake microservice names."""
        return "".join(
            [
                self.random_element(
                    [
                        "auth",
                        "authorisation",
                        "authentication",
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
                        "sales",
                        "sms",
                        "user",
                    ]
                ),
                self.random_element(["", "-", "_"]),
                self.random_element(
                    [
                        "adapter",
                        "api",
                        "bridge",
                        "interface",
                        "manager",
                        "platform",
                        "processor",
                        "service",
                        "ui",
                    ]
                ),
            ]
        )
