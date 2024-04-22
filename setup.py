# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PyGrammar",
    version="1.0",
    author="Mitchell Shibilski-Unkel",
    author_email="None",
    description="Python Grammar Bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MitchellShibilski-Unkel/PyGrammar",
    packages=find_packages(where="src"),  
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "nltk",
        "language_tool_python",
    ],
)
