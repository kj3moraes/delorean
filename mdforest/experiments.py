import re 
from treelib import Tree, Node

tree = Tree()

unique_id = 1

def build_tree(text:str, parent_id=None) -> Node:
    
    # Check if it is only text
    HEADER_PATTERN = r'^#+\s+(.*)$'
    matches = re.finditer(HEADER_PATTERN, text, re.MULTILINE)
        
    # Get all the indices of the headers
    indices = [(match.start(), match.end()) for match in matches]
    if len(indices) == 0:
        textnode = tree.create_node(text.strip()) if parent_id is None else tree.create_node(text, parent=parent_id)
        textnode.data = text.strip()
        return textnode
    
    # Get the first header
    first_header = text[indices[0][0]:indices[0][1]]
    firstHeaderLevel = len(first_header) - len(first_header.replace("#", ""))
    textnode = tree.create_node(first_header) if parent_id is None else tree.create_node(first_header, parent=parent_id)
    
    # Iterate over all the rest of the headers
    is_recursive = False
    for i in range(1, len(indices)):
        header = text[indices[i][0]:indices[i][1]]
        headerLevel = len(header) - len(header.replace("#", ""))
        
        if headerLevel > firstHeaderLevel:
            continue
        else:
            is_recursive = True
            text_extract = text[indices[i-1][1]:indices[i][0]].strip()
            textnode.data = text_extract
            child = build_tree(text_extract, textnode.identifier)
        
    if not is_recursive:
        text_extract = text.strip()
        textnode.data = text_extract
        child = build_tree(text_extract, textnode.identifier)
        
    return textnode

# def extract_text_up_to_header(markdown:str, parent_id=None):
   
#     sentences = markdown.splitlines()
#     text_extract = ""
#     currTree = Tree()
#     currTree.create_node("Root", id=unique_id)
#     unique_id += 1
    
#     # Check if it is only text
#     pattern = re.compile(r'^#+\s+(.*)$')
#     headers = list(filter(pattern.match, sentences))
#     if len(headers) == 0:
#         currTree.create_node(markdown) if parent_id is None else currTree.create_node(markdown, parent=parent_id)
#         return currTree
    
#     for i, sentence in enumerate(sentences):

#         if re.match(r'^#+\s+(.*)$', sentence):
#             currentHeaderLevel = len(sentence) - len(sentence.replace("#", ""))
#             currTree.create_node(sentence, identifier=i, parent='root')
#             for j in range(i + 1, len(sentences)):
#                 currSentence = sentences[j]
#                 if re.match(r'^#+\s+(.*)$', currSentence):
#                     headerLevel = len(currSentence) - len(currSentence.replace("#", ""))
#                     if headerLevel <= currentHeaderLevel:
#                         return text_extract
#                     else:
#                         text_extract += sentences[j] + "\n"
#                         currTree.create_node(currSentence, parent=i)
#                 else:
#                     text_extract += sentences[j] + "\n"
#                     currTree.create_node(currSentence, parent=i)
#         elif sentence != "":
#             currTree.create_node(sentence, parent='root')
                     
#     return text_extract

tree.create_node("Root", "root")

text = """
# Header 1
This is my first para
## Header 2
Then there was a second para
""".strip()

text2 = """
another piece of just text
wow.
"""

build_tree(text, 'root')
print(tree.show())
