from .markdown_tree import *
from .tree.types import *

def treeify(md:str, *args, **kwargs) -> MarkdownForest:
    """
    Converts markdown file to a Python object (MarkdownForest).
    """
    
    return mdtreeify(md, *args, **kwargs)

def mardownify(tree:MarkdownForest, *args, **kwargs) -> str:
    """
    Converts Python object (MarkdownForest) to markdown file.
    """
    
    return mdtextify(tree, *args, **kwargs)

