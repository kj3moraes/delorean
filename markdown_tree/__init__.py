from .treeify import treeify
from .tree.types import *

def treeify(md:str, *args, **kwargs) -> MarkdownForest:
    """
    Converts markdown file to a Python object (MarkdownForest).
    """
    return treeify(md, *args, **kwargs)

def mardownify(tree:MarkdownForest, *args, **kwargs) -> str:
    
    pass
