""" This file contains the main functions for the delorean package.
"""
    
import re

import frontmatter
from treelib import Tree
from .utils import *
from .tree import MarkdownForest, TextNode, HeaderNode
from .parser import *

# ==================================================================================================
#                                           TREEIFY
# ==================================================================================================

# TODO: Rename to snake_case in the future.


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
    
    if cont == "":
        # If the file is empty, just create a root node
        tree = Tree()
        tree.create_node(tag=name, identifier="root").identifier
    else:
        # Based on the file type specified by the user, choose a parser
        if 'type' in kwargs:
            if kwargs['type'] == FileType.MARKDOWN:
                parser = MarkdownParser(name, cont)
            elif kwargs['type'] == FileType.RESTRUCTUREDTEXT:
                parser = RestructuredParser(name, cont)
            elif kwargs['type'] == FileType.TXT:
                parser = TextParser(name, cont)
            elif kwargs['type'] == FileType.YAML:
                parser = YAMLParser(name, cont)
            else:
                raise ValueError("Invalid file type.")
        else:
            parser = MarkdownParser(name, cont)
            
        tree = parser.parse()
    
    returnForest = MarkdownForest(tree, name, metadata=meta)
    
    for backlink in backlinks:
        returnForest.add_backlink(backlink)
    for tag in tags:
        returnForest.add_tag(tag)

    return returnForest


# ==================================================================================================
#                                           TEXTIFY
# ==================================================================================================

def convertRootToText(rootNode: HeaderNode) -> str:
    
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
