from treebuild import TreeOfContents
from tree.types import MarkdownTree

def treeify(md:str, *args, **kwargs):
    """
    Converts markdown file to a Python object
    """
    return TreeOfContents.fromMarkdown(md, *args, **kwargs)

def mardownify(tree:MarkdownTree):
    pass
