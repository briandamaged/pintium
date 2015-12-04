from setuptools import setup, find_packages

setup(
    name = 'pintium',
    version = '2.0.0a2',
    description = 'Pinterest + Selenium = Pintium',
    author = 'Brian Lauber',
    author_email = 'constructible.truth@gmail.com',
    packages = find_packages(exclude = ["tests"]),
    install_requires = ["selenium", "requests"],
    test_suite = 'tests',
    tests_require = ["mock>=1.0.0"]
)
