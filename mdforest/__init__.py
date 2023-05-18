from .mdforest import *
from .tree.types import *

def treeify(name:str="[document]", md:str="", *args, **kwargs) -> MarkdownForest:
    """
    Converts markdown file to a Python object (MarkdownForest).
    """
    
    return mdtreeify(name, md, *args, **kwargs)

def markdownify(tree:MarkdownForest, *args, **kwargs) -> str:
    """
    Converts Python object (MarkdownForest) to markdown file.
    """
    
    return mdtextify(tree, *args, **kwargs)

