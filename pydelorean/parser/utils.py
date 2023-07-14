import re
from pydelorean.tree import TextNode, HeaderNode
from bigtree import Node, print_tree

def build_tree(inputText:str, *args, **kwargs) -> Node:

    assert isinstance(inputText, str), "inputText must be a string"
    if inputText == "":
        return None
    
    root = HeaderNode(header=kwargs["document_name"], headerNumber=0)

    # Default to the GFM header pattern
    HEADER_PATTERN = kwargs['header_pattern'] if 'header_pattern' in kwargs else r"^(#+\s+)(.*)"
    
    inputText = inputText.strip()
    matches = re.finditer(HEADER_PATTERN, inputText, re.MULTILINE)
        
    # Get all the indices of the headers
    indices = [(match.start(), match.end()) for match in matches]
    
    # BASE CASE
    # Check if it is only text (since there are no header indices)
    if len(indices) == 0:
        text_node = TextNode(name=inputText, text=inputText)
        root >> text_node
        root ** text_node
        return root
    
    # Is there text before the first header?
    if indices[0][0] != 0:
        textBefore = inputText[0:indices[0][0]]
        node = TextNode(name=textBefore, text=textBefore)
        root >> node
        root ** node

    # Use a stack to keep track of the header levels.
    stack = []

    # Iterate over all the headers and accordingly build the tree.
    for currHeader in indices:

        currHeaderText = inputText[currHeader[0]:currHeader[1]]
        currHeaderLevel = len(currHeaderText) - len(currHeaderText.replace("#", ""))
        
        # If this is the first header then create the header node automatically.
        if len(stack) == 0:
            
            # Create the header node with the current header.
            node = HeaderNode(header=currHeaderText, headerNumber=currHeaderLevel)
            root >> node
            root ** node
                        
            # Add the node to the stack
            stack.append((currHeaderLevel, currHeader, node))
            continue
        else:
            lastHeader = stack[-1]
        
        # CASE 1: If the current header level is greater than the starting header level then keep going.
        if currHeaderLevel > lastHeader[0]:
            
            # Extract the text between the current header and the previous header
            textBetween = inputText[lastHeader[1][1]:currHeader[0]].strip()
            if textBetween != "":
                node = TextNode(name=textBetween, text=textBetween)
                lastHeader[-1] >> node
                lastHeader[-1] ** node
                
            # Create the header node and add it to the stack
            node = HeaderNode(header=currHeaderText, headerNumber=currHeaderLevel)
            lastHeader[-1] >> node
            lastHeader[-1] ** node
            
            stack.append((currHeaderLevel, currHeader, node))
            
        # CASE 2: If the current header level is less than or equal to the starting header level then we need to create a new tree.
        elif currHeaderLevel <= lastHeader[0]:
            
            # Get the text between 
            textBetween = inputText[lastHeader[1][1]:currHeader[0]].strip()
            if textBetween != "":
                node = TextNode(name=textBetween, text=textBetween)
                lastHeader[-1] >> node
                lastHeader[-1] ** node
                                            
            # Pop off until you get to the node with a lower level than the current header level
            while len(stack) > 0:
                if stack[-1][0] >= currHeaderLevel:
                    stack.pop()
                else:
                    break
            
            if len(stack) == 0:
                
                node = HeaderNode(header=currHeaderText, headerNumber=currHeaderLevel)
                root >> node
                root ** node
            else:
                node = HeaderNode(header=currHeaderText, headerNumber=currHeaderLevel)
                stack[-1][-1] >> node
                stack[-1][-1] ** node
                
            stack.append((currHeaderLevel, currHeader, node))


    # Check if there is any text after the last header
    if indices[-1][1] != len(inputText):
        textEnd = inputText[indices[-1][1]:].strip()
        node = TextNode(name=textEnd, text=textEnd)
        stack[-1][-1] >> node
        stack[-1][-1] ** node
        
    return root

