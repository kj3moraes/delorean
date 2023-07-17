""" This file contains the main functions for the delorean package.
"""
from .files import *
from .base import *
from .parser import *
from .tools import *

# ==================================================================================================
#                                           TREEIFY
# ==================================================================================================

# TODO: Rename to snake_case in the future.

def mdtreeify(name:str, md:str, *args, **kwargs) -> MarkdownForest:
    """
    Converts markdown file to a MarkdownForest
    """
    
    meta, cont = find_metadata(md)
    
    backlinks = find_backlinks(cont)
    tags = find_tags(cont)
    
    if cont == "":
        # If the file is empty, just create a root node
        tree = Node("root")
        return tree
    
    
    parser = MarkdownParser(name, cont)
    tree = parser.parse()
    
    returnForest = MarkdownForest(tree, name, metadata=meta)
    
    for backlink in backlinks:
        returnForest.add_backlink(backlink)
    for tag in tags:
        returnForest.add_tag(tag)

    return returnForest


def rsttreeify(name:str, rst:str, *args, **kwargs) -> RestructuredForest:
    pass


def asciidoc_treeify(name:str, adoc:str, *args, **kwargs) -> AsciiDocForest:
    pass


def yaml_treeify(name:str, yaml:str, *args, **kwargs) -> YAMLForest:
    pass


def jsontreeify(name:str, json:str, *args, **kwargs) -> JSONForest:
    pass


# ==================================================================================================
#                                           TEXTIFY
# ==================================================================================================


def header_node_to_text(rootNode: HeaderNode) -> str:
    
    # BASE CASE: We just have text node.
    if isinstance(rootNode, TextNode):
        return rootNode.text + "\n\n"
    
    # For the header node
    headerLevel = rootNode.header_level
    returnString = str(rootNode) + "\n"
    for _, child in enumerate(rootNode.children):
        returnString += header_node_to_text(child)
    
    return returnString    
     

def convert_to_metadata(metadata_dict:dict) -> str:
    yaml = "---\n"
    for key, value in metadata_dict.items():
        
        if isinstance(value, list):
            yaml += f"{key}: \n"
            for elem in value:
                yaml += f"  - {elem}\n"
            continue
        
        yaml += f"{key}: {value}\n"
    yaml += "---\n"
    return yaml


def mdtextify(forest: MarkdownForest) -> str:
    """
    Converts a MarkdownForest to a markdown file.
    """
    
    returnString = ""
    
    # Get the root node
    root = forest.root
    
    # Get the metadata
    metadata = forest.get_metadata()
    returnString = convert_to_metadata(metadata) + "\n"
    
    for node in root.children:
        returnString += header_node_to_text(node) + "\n"
    
    return returnString


def rsttextify(forest: RestructuredForest) -> str:
    
    pass


def asciidoctextify(forest: AsciiDocForest) -> str:
    pass


def yamltextify(forest: YAMLForest) -> str:
    pass


def jsontextify(forest: JSONForest) -> str:
    pass

