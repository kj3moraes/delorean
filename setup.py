from setuptools import setup
from setuptools.command.test import test as TestCommand
from pathlib import Path

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.rst").read_text()

VERSION = '1.3.4'
DESCRIPTION = 'A package to convert between markup language documents and a forest data structure for efficient processing.'

setup(
    name = "pydelorean",
    version = VERSION,
    author = "Keane Moraes",
    author_email = 'lordvader3002@gmail.com',
    description = DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license = "Apache 2.0",
    url = "http://github.com/kj3moraes/delorean",
    packages = ['pydelorean', 'pydelorean.tree', 'pydelorean.parser', 'pydelorean.tools'],
    tests_require = ['unittest'],
    install_requires = ['markdown', 'bigtree', 'beautifulsoup4'],
    download_url = 'https://github.com/kj3moraes/delorean/archive/%s.zip' % VERSION,
    classifiers = [
        "Topic :: Utilities",
    ],
)
