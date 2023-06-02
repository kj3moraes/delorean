import os, sys
import mdforest 

def generate_forest(path_to_md_file:str):
    
    markdown_text = open(path_to_md_file, "r").read()

    name_of_file = os.path.basename(path_to_md_file)
    # Create a forest from the Markdown text
    forest = mdforest.treeify(name_of_file, markdown_text)
    print(forest)
    print("THE NUMBER OF TREES ARE", forest.treeCount)
    root = forest[0].root
    for branches in root.children:
        if isinstance(branches, mdforest.tree.HeaderNode):
            print(branches)
        elif isinstance(branches, mdforest.tree.TextNode):
            print(repr(branches))
    
    
# Iterate over all markdown files in the current directory
generate_forest("./kmag.md")
        

