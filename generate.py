import os, sys
from pydelorean import treeify, textify
from bigtree import print_tree, shift_nodes
from pydelorean.tools import get_progressive_expansion, clean_markdown


def generate_forest(path_to_md_file:str):
    
    markdown_text = open(path_to_md_file, "r").read()

    name_of_file = os.path.basename(path_to_md_file)
    # Create a forest from the Markdown text
    forest = treeify(name_of_file, markdown_text)
    
    root = forest.root
    print_tree(root)
    
    for children in root.children:
        print(children.path_name)
    
    expanse = get_progressive_expansion(root, append=True)

    for header, para in expanse:
        print(header, "\n=====================")
        print(clean_markdown(para, remove_header_tags=True))
        print()
    
    
# Iterate over all markdown files in the current directory
generate_forest("./samples/markdown/dune_appendices.md")
        

