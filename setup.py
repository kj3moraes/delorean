import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand
from pathlib import Path

class PyTest(TestCommand):

    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['tests']

    def finalize_options(self):
        TestCommand.finalize_options(self)

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

VERSION = '1.0.1'
DESCRIPTION = 'A package to convert between Markdown and a forest data structure for effecient processing.'

setup(
    name = "mdforest",
    version = VERSION,
    author = "Keane Moraes",
    author_email = 'lordvader3002@gmail.com',
    description = DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="Markdown",
    readme="README.md",
    license = "Apache 2.0",
    url = "http://github.com/kj3moraes/markdown-tree",
    packages = ['markdown_tree'],
    cmdclass = {'test': PyTest},
    tests_require = ['pytest'],
    install_requires = ['markdown', 'beautifulsoup4'],
    download_url = 'https://github.com/kj3moraes/markdown-tree/archive/%s.zip' % VERSION,
    classifiers = [
        "Topic :: Utilities",
    ],
)
