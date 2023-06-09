import os, sys
from pydelorean import treeify, textify
from bigtree import print_tree
from pydelorean.tools import get_progressive_expansion

def texting(text:str):
    print("got the text", text[:5])
    

def generate_forest(path_to_md_file:str):
    
    markdown_text = open(path_to_md_file, "r").read()

    name_of_file = os.path.basename(path_to_md_file)
    # Create a forest from the Markdown text
    forest = treeify(name_of_file, markdown_text)
    print(forest)
    
    root = forest.root
    # collection_rec(root, forest.root)
    
    print_tree(root)
    
    to_text = textify(forest)
    print(to_text)
    
    # first_child = forest.root.children(root.identifier)[0]
    # expanse = get_progressive_expansion(forest.root, first_child.identifier, append=True)

    # for node in expanse:
    #     print(f"{node}\n\n")
    
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
generate_forest("./samples/text1.md")
        

