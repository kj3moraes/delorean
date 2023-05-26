from bs4 import BeautifulSoup
from .mdforest import *
from .tree.types import *

def treeify(name:str="[document]", md:str="", *args, **kwargs) -> MarkdownForest:
    """
    Converts markdown file to a Python object (MarkdownForest).
    """
    
    return mdtreeify(name, md, *args, **kwargs)

def markdownify(tree:MarkdownForest, *args, **kwargs) -> str:
    """
    Converts Python object (MarkdownForest) to markdown file.
    """
    
    return mdtextify(tree, *args, **kwargs)

def clean_markdown(md:str) -> str:
    """
    Cleans markdown file of bold and italics formatting.
    """
        
    # Remove the metadata
    _, markdown_text = find_metadata(md)
    
     # Create a BeautifulSoup object with the input markdown text
    soup = BeautifulSoup(markdown_text, 'html.parser')

    # Remove HTML tags from the document
    markdown_text = soup.get_text()
    
    # Remove links
    markdown_text = re.sub(r'!\[(.*?)\]\((.*?)\)', '', markdown_text)
    markdown_text = re.sub(r'\[(.*?)\]\((.*?)\)', '', markdown_text)
    markdown_text = markdown_text.replace('>', '')
    
    # Remove bold and italics formatting
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'\1', markdown_text)
    markdown_text = re.sub(r'__(.*?)__', r'\1', markdown_text)
    markdown_text = re.sub(r'\*(.*?)\*', r'\1', markdown_text)
    markdown_text = re.sub(r'_(.*?)_', r'\1', markdown_text)
    
    # Remove empty lines
    markdown_text = re.sub(r'^\s*$', '', markdown_text, flags=re.MULTILINE)
    
    return markdown_text
    
