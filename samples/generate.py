import os, sys
import delorean 

def generate_forest(path_to_md_file:str):
    
    markdown_text = open(path_to_md_file, "r").read()

    name_of_file = os.path.basename(path_to_md_file)
    # Create a forest from the Markdown text
    forest = delorean.treeify(name_of_file, markdown_text)
    print(forest)
    
    
# Iterate over all markdown files in the current directory
generate_forest("./kmag.md")
        

