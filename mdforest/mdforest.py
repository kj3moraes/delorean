import frontmatter 
import re
from .treebuild import __TreeOfContents
from .tree.types import *

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
            resultNode = TextNode(child.source.string, parent=rootNode)
            corpus = resultNode.get_corpus()
            rootNode.append_corpus(corpus)
        else:
            resultNode = generateRootNodeFromContents(child, parent=rootNode)
            corpus = resultNode.get_corpus()
            rootNode.add_child(resultNode)
            rootNode.append_corpus(corpus)
                
    return rootNode    

def find_backlinks(input_text:str) -> list:
    """ 
    Function to find all backlinks in a given text.
    """
    
    backlinks = []

    # Regular expression pattern to match backlinks
    pattern = r'\[\[(.*?)\]\]'
    backlinks = re.findall(pattern, input_text)
    return backlinks

def find_tags(input_text:str) -> list:
    """
    Function to find all tags in a given text.
    """
    
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
        if isinstance(value, list):
            yaml += f"{key}: \n"
            for elem in value:
                yaml += f"  - {elem}\n"
            continue
        yaml += f"{key}: {value}\n"
    yaml += "---\n"
    return yaml

def mdtextify(forest:MarkdownForest, *args, **kwargs) -> str:
    
    finalText = convertDictToMetadata(forest.metadata)
    for i, tree in enumerate(forest):
        finalText += convertRootToText(tree.get_root())
    return finalText
