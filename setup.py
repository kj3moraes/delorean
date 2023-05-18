import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand
from pathlib import Path

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.rst").read_text()

VERSION = '1.3.1'
DESCRIPTION = 'A package to convert between Markdown and a forest data structure for efficient processing.'

setup(
    name = "mdforest",
    version = VERSION,
    author = "Keane Moraes",
    author_email = 'lordvader3002@gmail.com',
    description = DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    readme="README.rst",
    license = "Apache 2.0",
    url = "http://github.com/kj3moraes/markdown-tree",
    packages = ['mdforest', 'mdforest.tree'],
    tests_require = ['unittest', 'pytest'],
    install_requires = ['markdown', 'beautifulsoup4', 'python-frontmatter'],
    download_url = 'https://github.com/kj3moraes/markdown-tree/archive/%s.zip' % VERSION,
    classifiers = [
        "Topic :: Utilities",
    ],
)
