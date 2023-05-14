
from markdown_tree import *
import unittest

ORDERED_HIERARCHY = open("tests/docs/test_ordered.md", "r").read()

def test_treeify_ordered_hierarchy():

    a = treeify(ORDERED_HIERARCHY)
    primary_tree = a[0]
    assert str(primary_tree.get_root()) == "Header 1"
    assert str(primary_tree.get_root()[0]) == "Header 2.1"
    assert repr(primary_tree.get_root()[0][0]) == "Some text here and there"
    assert str(primary_tree.get_root()[0][1]) == "Header 3"
    assert str(primary_tree.get_root()[1]) == "Header 2.2"
    assert repr(primary_tree.get_root()[1][0]) == "Thats' all folks!"
    
def test_treeify_unordered_hierarchy():
    pass

def test_treeify_mixed_hierarchy():
    pass

def test_markdownify_ordered_hierarchy():
    a = treeify(ORDERED_HIERARCHY)
    ret_ordered = markdownify(a)
    assert ORDERED_HIERARCHY == ret_ordered

def test_markdownify_unordered_hierarchy():
    pass

def test_both_ordered_hierarchy():
    pass