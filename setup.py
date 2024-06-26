from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = 'v1.0'
DESCRIPTION = 'Python Grammar Bot'
LONG_DESCRIPTION = '-'

# Setting up
setup(
    name="PyGrammar",
    version=VERSION,
    author="Mitchell Shibilski-Unkel",
    author_email="None",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['nltk', 'language_tool_python'],
    keywords=['python', 'grammar', 'grammarbot'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
