from bs4 import BeautifulSoup
from .delorean import mdtreeify, find_metadata
from .tree import Forest
import re

def treeify(name:str, md:str, *args, **kwargs) -> Forest:
    
    return mdtreeify(name, md, *args, **kwargs)

# def markdownify(tree:MarkdownForest, *args, **kwargs) -> str:
#     """_summary_

#     Args:
#         tree (MarkdownForest): _description_

#     Returns:
#         str: _description_
#     """
    
#     return mdtextify(tree, *args, **kwargs)

def clean_markdown(md:str) -> str:
        
    # Remove the metadata
    _, markdown_text = find_metadata(md)
    
     # Create a BeautifulSoup object with the input markdown text
    soup = BeautifulSoup(markdown_text, 'html.parser')

    # Remove HTML tags from the document
    markdown_text = soup.get_text()
    
    # Remove links, images, and backlinks
    markdown_text = re.sub(r'!\[(.*?)\]\((.*?)\)', '', markdown_text)
    markdown_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', markdown_text)
    markdown_text = re.sub(r'\[\[(.*?)\]\]', r'\1', markdown_text)
    
    # Remove quotation marks
    markdown_text = markdown_text.replace('>', '')  
    
    # Remove bold and italics formatting
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'\1', markdown_text)
    markdown_text = re.sub(r'__(.*?)__', r'\1', markdown_text)
    markdown_text = re.sub(r'\*(.*?)\*', r'\1', markdown_text)
    markdown_text = re.sub(r'_(.*?)_', r'\1', markdown_text)
    
    # Remove empty lines
    markdown_text = re.sub(r'^\s*$', '', markdown_text, flags=re.MULTILINE)
    
    return markdown_text
    
