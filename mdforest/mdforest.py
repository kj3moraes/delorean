import frontmatter 
import re
from treebuild import __TreeOfContents
from tree.types import *

def generateRootNodeFromContents(currTree:__TreeOfContents, parent:Node=None) -> Node:
    """ Function to generate the tree of a specific header's section.
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

def find_backlinks(input_text:str) -> list:
    backlinks = []

    # Regular expression pattern to match backlinks
    pattern = r'\[\[(.*?)\]\]'
    backlinks = re.findall(pattern, input_text)

    return backlinks

def find_tags(input_text:str) -> list:
    tags = []

    # Regular expression pattern to match backlinks
    pattern = r'#([a-zA-Z0-9_]+)'
    tags = re.findall(pattern, input_text)
    return tags

def mdtreeify(name:str, md:str, *args, **kwargs) -> MarkdownForest:
    """
    Converts markdown file to a MarkdownForest
    """
    
    post = frontmatter.loads(md)
    backlinks = find_backlinks(post.content)
    tags = find_tags(post.content)
    returnForest = MarkdownForest(name, metadata=post.metadata)
    for backlink in backlinks:
        returnForest.add_backlink(backlink)
    for tag in tags:
        returnForest.add_tag(tag)
    toc =  __TreeOfContents.fromMarkdown(post.content, *args, **kwargs)
    for tree in toc.branches:
        root = generateRootNodeFromContents(tree)
        returnForest.add_tree(MarkdownTree(root))
    return returnForest
    
def convertRootToText(rootNode: Node) -> str:
    
    # BASE CASE: We just have text node.
    if isinstance(rootNode, TextNode):
        return repr(rootNode) + "\n"
    
    # For the header node
    headerLevel = rootNode.get_header_level()
    returnString = '#'*headerLevel + " " + str(rootNode) + "\n"
    for i, child in enumerate(rootNode):
        returnString += convertRootToText(child)
    
    return returnString    
        
def convertDictToMetadata(metadata:dict) -> str:
    yaml = "---\n"
    for key, value in metadata.items():
        print(f"{key}: {value}")
        if isinstance(value, list):
            yaml += f"{key}: \n"
            for elem in value:
                yaml += f"  - {elem}\n"
            continue
        yaml += f"{key}: {value}\n"
    yaml += "---\n"
    return yaml

def mdtextify(forest:MarkdownForest, *args, **kwargs) -> str:
    print(forest.metadata)
    
    finalText = convertDictToMetadata(forest.metadata)
    for i, tree in enumerate(forest):
        finalText += convertRootToText(tree.get_root())
    return finalText
        
# test = """# Header 1
# ## Header 2.1
# Some text here and there
# ### Header 3
# Some more text here and there
# ## Header 2.2
# Thats' all folks!
# """

# test2 = """
# ---
# tags: [test, test2, test3]
# author: Keane Moraes
# time: 2
# ---
# # Header 1
# ## Header 2.1
# Some [[text]] here and there #asd
# ### Header 3
# Some more text here and there
# ## Header 2.2
# Thats' all folks!
# """

# print(find_tags(test2))

# a = mdtreeify("test2", test2)
# print(a)
# print(mdtextify(a))
# print(a)
# ret_test2 = mdtextify(a)

# print(ret_test2)

# print(a)
# a[0].root.add_child(TextNode("asdasd", parent=a[0].root))
# print(a)