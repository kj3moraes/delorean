import os, sys
import mdforest 
import mdforest.tree as mdtree

def generate_forest(path_to_md_file:str):
    
    markdown_text = open(path_to_md_file, "r").read()

    name_of_file = os.path.basename(path_to_md_file)
    # Create a forest from the Markdown text
    forest = mdforest.treeify(name_of_file, markdown_text)
    print(forest)
    print("THE NUMBER OF TREES ARE", forest.treeCount)
    root = forest[0].get_root()
    print(root.get_corpus())
    print(forest[1].get_root().get_corpus())
    print(forest.get_backlinks())
    
    
# Iterate over all markdown files in the current directory
for filename in os.listdir("."):
    if filename.endswith(".md"):
        generate_forest(filename)
        

