
from markdown_tree import *
import unittest

def test_ordered_hierarchy():
    test_str = """# Header 1
## Header 2.1
Some text here and there
### Header 3
Some more text here and there
## Header 2.2
Thats' all folks!
    """
    a = treeify(test_str)
    print(a)
    print("The header is ", a[0].get_root().__str__())
    assert str(a[0].get_root()) == "(h1) Header 1"
    assert str(a[0].get_root()[0]) == "(h2) Header 2.1"
