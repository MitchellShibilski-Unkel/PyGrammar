from setuptools import setup


setup(
    name="PyGrammar",
    version="1.0",
    author="Mitchell Shibilski-Unkel",
<<<<<<< Updated upstream
    py_modules=['src.PyGrammar']
=======
    setup_requires=['src'],
    py_modules=['PyGrammar'],
    package_dir={'src'},
>>>>>>> Stashed changes
)
