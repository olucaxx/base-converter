from setuptools import setup

setup(
    name="base-converter",
    version="0.1.0",
    packages=["base_converter"],
    entry_points={
        "console_scripts": [
            "base-converter=base_converter.main:main"
        ]
    },
)
