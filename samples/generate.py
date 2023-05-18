import os, sys
import mdforest 
import mdforest.tree as mdtree

def generate_forest(path_to_md_file:str):
    
    markdown_text = open(path_to_md_file, "r").read()
    # print(markdown_text)
    name_of_file = os.path.basename(path_to_md_file)
    # Create a forest from the Markdown text
    forest = mdforest.treeify(name_of_file, markdown_text)
    # print(forest)
    
    
# Iterate over all markdown files in the current directory
for filename in os.listdir("."):
    if filename.endswith(".md"):
        generate_forest(filename)
        

