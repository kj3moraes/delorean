
from markdown_tree import treeify 

def test_ordered_hierarchy():
    test_str = """
    # Header 1
    ## Header 2.1
    Some text here and there
    ### Header 3
    Some more text here and there
    ## Header 2.2
    Thats' all folks!
    """
    a = treeify(test_str)
    self.assertEqual(a[0].root.__str__(), "Header 1")
    pass

def test_unordered_hierarchy():
    pass

def test_mixed_hierarchy():
    pass

def test_ordered_hierarchy():
    pass

def test_unordered_hierarchy():
    pass

def test_mixed_hierarchy():
    pass


def test_ordered_hierarchy():
    pass

def test_unordered_hierarchy():
    pass

def test_mixed_hierarchy():
    pass