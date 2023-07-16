from pydelorean.base.node import *
from bs4 import BeautifulSoup
import re
import frontmatter

def get_progressive_expansion(node:Node, **kwargs) -> list:
    
    # BASE CASE: TextNode
    if isinstance(node, TextNode):
        return [(node.corpus, node.corpus)]
    
    if kwargs.get("append", False):
        returned_list = [(node.header, node.corpus)]
    else:
        returned_list = []
    for child in node.children:
        if isinstance(child, HeaderNode):
            child_list = get_progressive_expansion(child, append=True)
            returned_list += [(child.header, para) for header, para in child_list]
        elif isinstance(child, TextNode):
            returned_list.append((node.header, child.corpus))
        
    return returned_list


def find_backlinks(input_text:str) -> list:
    """ 
    Function to find all backlinks in a given text.
    """
    
    backlinks = []

    # Regular expression pattern to match backlinks
    pattern = r'\[\[(.*?)\]\]'
    backlinks = re.findall(pattern, input_text)
    return backlinks


def find_tags(input_text:str) -> list:
    """
    Function to find all tags in a given text.
    """
    
    tags = []

    # Regular expression pattern to match backlinks
    pattern = r'#([a-zA-Z0-9_]+)'
    tags = re.findall(pattern, input_text)
    return tags


def find_metadata(input_text:str):
    post = frontmatter.loads(input_text)
    return post.metadata, post.content


def clean_markdown(md:str, **kwargs) -> str:
        
    remove_header_tags = kwargs.get("remove_header_tags", False)    
    
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
    
    # Remove header tags
    if remove_header_tags:
        markdown_text = re.sub(r'#+', '', markdown_text)
    
    return markdown_text

