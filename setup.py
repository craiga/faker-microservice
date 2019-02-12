"""Provider for Faker which adds fake microservice names."""

import setuptools

try:
    with open("README.markdown", "r") as fh:
        long_description = fh.read()  # pylint: disable=invalid-name
except FileNotFoundError:
    pass

setuptools.setup(
    name="faker-microservice",
    version="1.0.2",
    author="Craig Anderson",
    author_email="craiga@craiga.id.au",
    description="Provider for Faker which adds fake microservice names.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/craiga/faker-microservice",
    packages=setuptools.find_packages(),
    install_requires=["faker"],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
