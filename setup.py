"""Provider for Faker which adds fake microservice names."""

import setuptools

with open("README.markdown", "r") as fh:
    long_description = fh.read()  # pylint: disable=invalid-name

setuptools.setup(
    name="faker-microservice",
    version="1.0.0",
    author="Craig Anderson",
    author_email="craiga@craiga.id.au",
    description="Provider for Faker which adds fake microservice names.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/craiga/faker-microservice",
    packages=setuptools.find_packages(),
    install_requires=["faker"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
