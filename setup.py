import setuptools

setuptools.setup(
    name="pygrammar",
    version="1.0",
    author="Mitchell Shibilski-Unkel",
    author_email="",
    description="PyGrammar",
    long_description="Grammar Correction Library",
    url="https://github.com/MitchellShibilski-Unkel/PyGrammar.git",
    packages=setuptools.find_packages(),
    #install_requires=['transformers', 'sentencepiece==0.1.95', 'python-Levenshtein==0.12.2', 'fuzzywuzzy==0.18.0',  'tokenizers==0.10.2', 'fsspec==2021.5.0', 'lm-scorer==0.4.2', 'errant'],
    install_requires=['nltk', 'language_tool_python'],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: MIT",
        "Operating System :: OS Independent",
    ],
)

