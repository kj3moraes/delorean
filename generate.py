import os, sys
from pydelorean import treeify
from pydelorean.tree.types import TextNode, HeaderNode
from treelib import Tree, Node

def texting(text:str):
    print("got the text", text[:5])

def collection_rec(node:Node, tree:Tree):
    children = node.successors(tree.identifier)
    child_nodes = [tree.get_node(child) for child in children]
    for child in child_nodes:
        if isinstance(child.data, TextNode):
            texting(child.data.text)
        elif isinstance(child.data, HeaderNode):
            print("got the header", child.data)
            collection_rec(child, tree)
    

def generate_forest(path_to_md_file:str):
    
    markdown_text = open(path_to_md_file, "r").read()

    name_of_file = os.path.basename(path_to_md_file)
    # Create a forest from the Markdown text
    forest = treeify(name_of_file, markdown_text)
    print(forest)
    
    root = forest.root.get_node('root')
    collection_rec(root, forest.root)
    # tree_id = forest.root.identifier
    # children = root.successors(tree_id)
    # print(children)
    
    # for child in children:
    #     print("The data pf the root child is", child.data)
    #     sub_children = child.successors(tree_id)
    #     subnodes = []
    #     for sub_child in sub_children:
    #         subnodes.append(root.get_node(sub_child))
    #     print(f"\nThe children of the root child are {subnodes}\n")
    # print(child for child in children)
    # for child in root.all_nodes_itr():
    #     print(child.data)
    
    
# Iterate over all markdown files in the current directory
generate_forest("./samples/empty.md")
        

