# faker-microservice

Provider for [Faker](https://faker.readthedocs.io/) which adds fake microservice names.

[![PyPI](https://img.shields.io/pypi/v/faker-microservice.svg)](https://pypi.org/project/faker-microservice/)
![](https://img.shields.io/pypi/pyversions/faker-microservice.svg)
[![Downloads](https://pepy.tech/badge/faker-microservice)](https://pepy.tech/project/faker-microservice)
[![Build Status](https://img.shields.io/travis/com/craiga/faker-microservice.svg)](https://travis-ci.com/craiga/faker-microservice)
[![Maintainability](https://img.shields.io/codeclimate/maintainability/craiga/faker-microservice.svg)](https://codeclimate.com/github/craiga/faker-microservice/maintainability)
[![Test Coverage](https://img.shields.io/codeclimate/coverage/craiga/faker-microservice.svg)](https://codeclimate.com/github/craiga/faker-microservice/test_coverage)

# Installation

```
pipenv install faker-microservice
```

# Usage

## Python

```python
from faker import Faker

import faker_microservice

fake = Faker()
fake.add_provider(faker_microservice.Provider)
print(fake.microservice())  # prints "fulfilment_manager" or similar
```

## Command Line

```
pipenv run faker microservice -i faker_microservice
```
