# faker-microservice

Provider for Faker which adds fake microservice names.

[![Build Status](https://img.shields.io/travis/com/craiga/faker-microservice.svg)](https://travis-ci.com/craiga/faker-microservice)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Installation

    pip install faker-microservice

# Usage

    from faker import Faker

    from faker_microservice import MicroserviceProvider

    fake = Faker()
    fake.add_provider(MicroserviceProvider)
    print(fake.microservice())  # prints "fulfilment_manager" or similar
