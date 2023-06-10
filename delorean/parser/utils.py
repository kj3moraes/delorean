import re
from treelib import Tree
from delorean.tree import TextNode, HeaderNode


def buildTree(inputText:str, name:str, *args, **kwargs) -> Tree:
    """ Function to build the provides tree varaible from the inputText. 
    Works for Github Flavored Markdown (GFM). 

    Args:
        inputText (str): Input text to be parsed
        name (Str): Name of the document
        
    """
    assert isinstance(inputText, str), "inputText must be a string"
    if inputText == "":
        return None
    
    tree = Tree()
    root_id = tree.create_node(tag=name, identifier="root").identifier

    # Default to the GFM header pattern
    HEADER_PATTERN = kwargs['header_pattern'] if 'header_pattern' in kwargs else r"^(#+\s+)(.*)"
    
    matches = re.finditer(HEADER_PATTERN, inputText, re.MULTILINE)
        
    # Get all the indices of the headers
    indices = [(match.start(), match.end()) for match in matches]
    
    # BASE CASE
    # Check if it is only text (since there are no header indices)
    if len(indices) == 0:
        tree.create_node(tag=inputText[0:min(10, len(inputText))],
                         data=TextNode(inputText),
                         parent=root_id)
        return tree
    
    # Is there text before the first header?
    if indices[0][0] != 0:
        textBefore = inputText[0:indices[0][0]]
        tree.create_node(tag=textBefore[0:min(10, len(textBefore))],
                        data=TextNode(textBefore),
                        parent=root_id)

    # Use a stack to keep track of the header levels.
    stack = []

    # Iterate over all the headers and accordingly build the tree.
    for currHeader in indices:
   
        currHeaderText = inputText[currHeader[0]:currHeader[1]]
        currHeaderLevel = len(currHeaderText) - len(currHeaderText.replace("#", ""))
        
        # If this is the first header then create the root node automatically.
        if len(stack) == 0:
             # Create the header node with the current header.
            node = tree.create_node(tag=currHeaderText,
                                    data=HeaderNode(currHeaderText, currHeaderLevel, root_id),
                                    parent=root_id)

            # Add the node to the stack
            stack.append((currHeaderLevel, currHeader, node.identifier))
            continue
        else:
            lastHeader = stack[-1]
        
        # CASE 1: If the current header level is greater than the starting header level then keep going.
        if currHeaderLevel > lastHeader[0]:
            
            # Extract the text between the current header and the previous header
            textBetween = inputText[lastHeader[1][1]:currHeader[0]].strip()
            if textBetween != "":
                tree.create_node(tag=textBetween[0:min(10, len(textBetween))],
                                 data=TextNode(textBetween),
                                 parent=lastHeader[-1])

            # Create the header node and add it to the stack
            node = tree.create_node(tag=currHeaderText,
                                    data=HeaderNode(currHeaderText, currHeaderLevel, lastHeader[-1]),
                                    parent=lastHeader[-1])
            stack.append((currHeaderLevel, currHeader, node.identifier))
            
        # CASE 2: If the current header level is less than or equal to the starting header level then we need to create a new tree.
        elif currHeaderLevel <= lastHeader[0]:
            
            # Get the text between 
            textBetween = inputText[lastHeader[1][1]:currHeader[0]].strip()
            if textBetween != "":
                tree.create_node(tag=textBetween[0:min(10, len(textBetween))],
                                 data=TextNode(textBetween),
                                 parent=lastHeader[-1])
            
            # Pop off until you get to the node with a lower level than the current header level
            while len(stack) > 0:
                if stack[-1][0] >= currHeaderLevel:
                    stack.pop()
                else:
                    break
            
            if len(stack) == 0:
                
                node = tree.create_node(currHeaderText, data=HeaderNode(currHeaderText, currHeaderLevel, root_id), parent=root_id)
            else:
                node = tree.create_node(currHeaderText, data=HeaderNode(currHeaderText, currHeaderLevel, stack[-1][-1]), parent=stack[-1][-1])
            stack.append((currHeaderLevel, currHeader, node.identifier))
                
                
    # Check if there is any text after the last header
    if indices[-1][1] != len(inputText):
        textEnd = inputText[indices[-1][1]:].strip()
        tree.create_node(tag=textEnd[:min(10, len(textEnd))], data=TextNode(textEnd), parent=stack[-1][-1])
        
    return tree
