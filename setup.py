from setuptools import setup, find_packages

setup(
    name="humanizer",
    version="1.0.0",
    description="Automates text processing using Humanize AI.",
    packages=find_packages(),
    install_requires=[
        "playwright"
    ],
    entry_points={
        "console_scripts": [
            "humanizer=humanizer.humanizer:main"
        ]
    },
)
