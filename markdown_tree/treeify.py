from treebuild import TreeOfContents
from tree.types import *

def treeify(md:str, *args, **kwargs):
    """
    Converts markdown file to a Python object
    """
    toc =  TreeOfContents.fromMarkdown(md, *args, **kwargs)
    highestHeader = toc.parseTopDepth()
    if highestHeader == None:
        print("No headers found")
        return MarkdownTree(TextNode(md))
    
    highestSection = toc.__getattr__(f"h{highestHeader}")
    root = HeaderNode(highestSection.string)
    
    numChildren = len(highestSection.branches)
    print("THE NUMBER OF CHILDREN", numChildren)  
    for i in range(numChildren):
        child = highestSection.branches[i]
        if child.name == f"h{highestHeader+1}":
            print("HEADER FOUND")
            root.add_child(HeaderNode(child.string))
        else:
            print("TEXT FOUND")
            root.add_child(TextNode(child.string))
        
    
    return MarkdownTree(root)
    
    
        
test = """
# Header 1
## Header 2
### Header 3
"""

test2 = """
### Header 3
Just text
"""

a = treeify(test2)
print(a)