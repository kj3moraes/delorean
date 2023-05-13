from .treebuild import TreeOfContents
from .tree.types import *

def generateRootNodeFromContents(currTree:TreeOfContents, parent:Node=None) -> Node:
    """ Function to generate the tree of a specfic header's section.
    """    
    # BASE CASE: If there is no depth, then it is just a paragraph
    if currTree.depth == None:
        return TextNode(currTree.source.string, parent=parent)
    
    # Get the current header of the tree
    headerText = currTree.source.string
    currentHeaderLevel = currTree.getHeadingLevel(currTree.source)
    rootNode = HeaderNode(headerText, headerNumber=currentHeaderLevel, parent=parent)
    
    for child in currTree.branches:
        if child.getHeadingLevel(child.source) == None:
            rootNode.add_child(TextNode(child.source.string, parent=rootNode))
        else:
            rootNode.add_child(generateRootNodeFromContents(child, parent=rootNode))
            
    return rootNode

def mdtreeify(md:str, *args, **kwargs) -> MarkdownForest:
    """
    Converts markdown file to a MarkdownForest
    """

    returnForest = MarkdownForest("test2")
    toc =  TreeOfContents.fromMarkdown(md, *args, **kwargs)
    for tree in toc.branches:
        root = generateRootNodeFromContents(tree)
        returnForest.add_tree(MarkdownTree(root))
        
    return returnForest
    
def mdtextify(tree:MarkdownForest, *args, **kwargs) -> str:
    pass
        
# test = """# Header 1
# ## Header 2.1
# Some text here and there
# ### Header 3
# Some more text here and there
# ## Header 2.2
# Thats' all folks!
# """

# test2 = """
# # asdasd
# ok then
# ## 1238123
# """

# a = mdtreeify(test)

# print(a)
# a[0].root.add_child(TextNode("asdasd", parent=a[0].root))
# print(a)