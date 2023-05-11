from treebuild import TreeOfContents
from tree.types import MarkdownTree

def treeify(md:str, *args, **kwargs):
    """
    Converts markdown file to a Python object
    """
    toc =  TreeOfContents.fromMarkdown(md, *args, **kwargs)
    highestHeader = toc.parseTopDepth()
    print(highestHeader)
    
    
test = """
# Header 1
## Header 2
### Header 3
"""

test2 = """
Just text
"""

treeify(test2)