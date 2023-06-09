""" This file contains the main functions for the mdforest package.
"""
    
import re

import frontmatter
from treelib import Tree

from .tree.types import MarkdownForest, TextNode, HeaderNode, Node

# ==================================================================================================
#                                           TREEIFY
# ==================================================================================================

# TODO: Rename to snake_case in the future.

def buildTree(inputText:str, tree:Tree, root_id) :
    """ Function to build the provides tree varaible from the inputText. 
    Works for Github Flavored Markdown (GFM). 

    Args:
        inputText (str): Input GFM text
        tree (Tree): treelib Tree object with root node
        root_id (_type_): id of the root node

    """
    assert isinstance(inputText, str), "inputText must be a string"
    # assert inputText != "", "inputText cannot be an empty string"
    if inputText == "":
        return []

    HEADER_PATTERN = r'^#+\s+(.*)$'
    
    matches = re.finditer(HEADER_PATTERN, inputText, re.MULTILINE)
        
    # Get all the indices of the headers
    indices = [(match.start(), match.end()) for match in matches]
    
    # BASE CASE
    # Check if it is only text (since there are no header indices)
    if len(indices) == 0:
        tree.create_node(tag=inputText[0:min(10, len(inputText))],
                         data=TextNode(inputText),
                         parent=root_id)
        return
    
    # Is there text before the first header?
    if indices[0][0] != 0:
        textBefore = inputText[0:indices[0][0]]
        tree.create_node(tag=textBefore[0:min(10, len(textBefore))],
                        data=TextNode(textBefore),
                        parent=root_id)

    stack = []

    for currHeader in indices:
   
        currHeaderText = inputText[currHeader[0]:currHeader[1]]
        currHeaderLevel = len(currHeaderText) - len(currHeaderText.replace("#", ""))
        
        # If this is the first header then create the root node automatically.
        if len(stack) == 0:
             # Create the header node with the current header.
            node = tree.create_node(tag=currHeaderText,
                                    data=HeaderNode(currHeaderText, currHeaderLevel, root_id),
                                    parent=root_id)

            # Add the node to the stack
            stack.append((currHeaderLevel, currHeader, node.identifier))
            continue
        else:
            lastHeader = stack[-1]
        
        # CASE 1: If the current header level is greater than the starting header level then keep going.
        if currHeaderLevel > lastHeader[0]:
            
            # Extract the text between the current header and the previous header
            textBetween = inputText[lastHeader[1][1]:currHeader[0]].strip()
            if textBetween != "":
                tree.create_node(tag=textBetween[0:min(10, len(textBetween))],
                                 data=TextNode(textBetween),
                                 parent=lastHeader[-1])

            # Create the header node and add it to the stack
            node = tree.create_node(tag=currHeaderText,
                                    data=HeaderNode(currHeaderText, currHeaderLevel, lastHeader[-1]),
                                    parent=lastHeader[-1])
            stack.append((currHeaderLevel, currHeader, node.identifier))
            
        # CASE 2: If the current header level is less than or equal to the starting header level then we need to create a new tree.
        elif currHeaderLevel <= lastHeader[0]:
            
            # Get the text between 
            textBetween = inputText[lastHeader[1][1]:currHeader[0]].strip()
            if textBetween != "":
                tree.create_node(tag=textBetween[0:min(10, len(textBetween))],
                                 data=TextNode(textBetween),
                                 parent=lastHeader[-1])
            
            # Pop off until you get to the node with a lower level than the current header level
            while len(stack) > 0:
                if stack[-1][0] >= currHeaderLevel:
                    stack.pop()
                else:
                    break
            
            if len(stack) == 0:
                node = tree.create_node(currHeaderText, data=HeaderNode(currHeaderText, currHeaderLevel, root_id), parent=root_id)
            else:
                node = tree.create_node(currHeaderText, data=HeaderNode(currHeaderText, currHeaderLevel, stack[-1][-1]), parent=stack[-1][-1])
            stack.append((currHeaderLevel, currHeader, node.identifier))
                
                
    # Check if there is any text after the last header
    if indices[-1][1] != len(inputText):
        textEnd = inputText[indices[-1][1]:].strip()
        tree.create_node(tag=textEnd[:min(10, len(textEnd))], data=TextNode(textEnd), parent=stack[-1][-1])


def findBacklinks(input_text:str) -> list:
    """ 
    Function to find all backlinks in a given text.
    """
    
    backlinks = []

    # Regular expression pattern to match backlinks
    pattern = r'\[\[(.*?)\]\]'
    backlinks = re.findall(pattern, input_text)
    return backlinks

def findTags(input_text:str) -> list:
    """
    Function to find all tags in a given text.
    """
    
    tags = []

    # Regular expression pattern to match backlinks
    pattern = r'#([a-zA-Z0-9_]+)'
    tags = re.findall(pattern, input_text)
    return tags

def findMetadata(input_text:str):
    post = frontmatter.loads(input_text)
    return post.metadata, post.content

def mdtreeify(name:str, md:str, *args, **kwargs) -> Tree:
    """
    Converts markdown file to a MarkdownForest
    """
    
    meta, cont = findMetadata(md)
    
    backlinks = findBacklinks(cont)
    tags = findTags(cont)
    tree = Tree()
    tree.create_node(name, "root")
    buildTree(cont, tree, "root")
    returnForest = MarkdownForest(tree, name, metadata=meta)
    
    for backlink in backlinks:
        returnForest.add_backlink(backlink)
    for tag in tags:
        returnForest.add_tag(tag)

    return returnForest


# ==================================================================================================
#                                           TEXTIFY
# ==================================================================================================

def convertRootToText(rootNode: Node) -> str:
    
    # BASE CASE: We just have text node.
    if isinstance(rootNode, TextNode):
        return repr(rootNode) + "\n"
    
    # For the header node
    headerLevel = rootNode.get_header_level()
    returnString = '#'*headerLevel + " " + str(rootNode) + "\n"
    for _, child in enumerate(rootNode):
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

# FIXME: Change the mdtextify implenmentation to use the new tree structure.
# def mdtextify(forest:MarkdownForest, *args, **kwargs) -> str:
    
#     finalText = convertDictToMetadata(forest.metadata)
#     for i, tree in enumerate(forest):
#         finalText += convertRootToText(tree.get_root())
#     return finalText
