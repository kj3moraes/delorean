from treebuild import TreeOfContents
from tree.types import *

def generateRootNode(currTree:TreeOfContents) -> HeaderNode | TextNode:
    """ Function to generate the tree of a specfic header's section.
    """    
    # BASE CASE: If there is no depth, then it is just a paragraph
    if currTree.depth == None:
        return TextNode(currTree.source.string)
    
    # Get the current header of the tree
    headerText = currTree.source.string
    rootNode = HeaderNode(headerText)
    
    for child in currTree.branches:
        # print("child is of instance ", type(child))
        # print("child is ", child.source.string)
        # print("child depth is ", child.getHeadingLevel(child.source))
        if child.getHeadingLevel(child.source) == None:
            rootNode.add_child(TextNode(child.source.string))
        else:
            rootNode.add_child(generateRootNode(child))
            
    return rootNode


def treeify(md:str, *args, **kwargs) -> MarkdownForest:
    """
    Converts markdown file to a MarkdownForest
    """
    
    returnForest = MarkdownForest()
    toc =  TreeOfContents.fromMarkdown(md, *args, **kwargs)
    for tree in toc.branches:
        root = generateRootNode(tree)
        print(MarkdownTree(root))
        
    return returnForest
    
    
        
test = """
# Header 1
## Header 2
### Header 3
"""

test2 = """
# asdasd
## 1238123
asdasdad
## 91892301
#### -0123123
# 01002
"""

a = treeify(test2)

print(a)