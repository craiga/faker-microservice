# faker-microservice

Provider for [Faker](https://faker.readthedocs.io/) which adds fake microservice names.

[![Build Status](https://img.shields.io/travis/com/craiga/faker-microservice.svg)](https://travis-ci.com/craiga/faker-microservice) [![Maintainability](https://img.shields.io/codeclimate/maintainability/craiga/faker-microservice.svg)](https://codeclimate.com/github/craiga/faker-microservice/maintainability) [![Test Coverage](https://img.shields.io/codeclimate/coverage/craiga/faker-microservice.svg)](https://codeclimate.com/github/craiga/faker-microservice/test_coverage) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Installation

    pip install faker-microservice

# Usage

    from faker import Faker

    from faker_microservice import MicroserviceProvider

    fake = Faker()
    fake.add_provider(MicroserviceProvider)
    print(fake.microservice())  # prints "fulfilment_manager" or similar
