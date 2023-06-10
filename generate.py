import os, sys
from delorean import treeify

def generate_forest(path_to_md_file:str):
    
    markdown_text = open(path_to_md_file, "r").read()

    name_of_file = os.path.basename(path_to_md_file)
    # Create a forest from the Markdown text
    forest = treeify(name_of_file, markdown_text)
    print(forest)
    root = forest.root
    for child in root.all_nodes_itr():
        print(child.data)
    
    
# Iterate over all markdown files in the current directory
generate_forest("./samples/text1.md")
        

