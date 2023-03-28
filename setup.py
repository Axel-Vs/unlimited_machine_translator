from setuptools import setup, find_packages

setup(
    name="unlimited_machine_translator",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[
        "deep_translator",
        "pandas",
        "numpy",
        "nltk",
        "python-docx",
    ],
)