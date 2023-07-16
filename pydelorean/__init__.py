from bs4 import BeautifulSoup
from .delorean import *
from .base import Forest
import re


# TODO: Check the type of the input and call the appropriate function
# Use the newly defined File classes for this. 
def treeify(name:str, text:str, *args, **kwargs) -> Forest:
    
    return mdtreeify(name, text, *args, **kwargs)


def textify(forest:Forest, *args, **kwargs) -> str:
    
    return mdtextify(forest)


# TODO: I want to only expose treeify and textify to the user. Move this someplace else.
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
    
