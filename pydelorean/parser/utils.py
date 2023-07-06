import re
from pydelorean.tree import TextNode, HeaderNode
from bigtree import Node, print_tree

def buildTree(inputText:str, *args, **kwargs) -> HeaderNode:
    """ Function to build the provides tree varaible from the inputText. 
    Works for Github Flavored Markdown (GFM). 

    Args:
        inputText (str): Input text to be parsed
        name (Str): Name of the document
        
    """
    assert isinstance(inputText, str), "inputText must be a string"
    if inputText == "":
        return None
    
    root = Node("root")

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
        return root
    
    # Is there text before the first header?
    if indices[0][0] != 0:
        textBefore = inputText[0:indices[0][0]]
        node = TextNode(name=textBefore, text=textBefore)
        root >> node

    # Use a stack to keep track of the header levels.
    stack = []

    # Iterate over all the headers and accordingly build the tree.
    for currHeader in indices:
   
        currHeaderText = inputText[currHeader[0]:currHeader[1]]
        currHeaderLevel = len(currHeaderText) - len(currHeaderText.replace("#", ""))
        
        # If this is the first header then create the header node automatically.
        if len(stack) == 0:
             # Create the header node with the current header.
            node = HeaderNode(name=currHeaderText, header=currHeaderText, headerNumber=currHeaderLevel)
            root >> node

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

            # Create the header node and add it to the stack
            node = HeaderNode(name=currHeaderText, header=currHeaderText, headerNumber=currHeaderLevel)
            lastHeader[-1] >> node
            
            stack.append((currHeaderLevel, currHeader, node))
            
        # CASE 2: If the current header level is less than or equal to the starting header level then we need to create a new tree.
        elif currHeaderLevel <= lastHeader[0]:
            
            # Get the text between 
            textBetween = inputText[lastHeader[1][1]:currHeader[0]].strip()
            if textBetween != "":
                node = TextNode(name=textBetween, text=textBetween)
                lastHeader[-1] >> node
                            
            # Pop off until you get to the node with a lower level than the current header level
            while len(stack) > 0:
                if stack[-1][0] >= currHeaderLevel:
                    stack.pop()
                else:
                    break
            
            if len(stack) == 0:
                
                node = HeaderNode(name=currHeaderText, header=currHeaderText, headerNumber=currHeaderLevel)
                root >> node
            else:
                node = HeaderNode(name=currHeaderText, header=currHeaderText, headerNumber=currHeaderLevel)
                stack[-1][-1] >> node
            stack.append((currHeaderLevel, currHeader, node))
                
                
    # Check if there is any text after the last header
    if indices[-1][1] != len(inputText):
        textEnd = inputText[indices[-1][1]:].strip()
        node = TextNode(name=textEnd, text=textEnd)
        stack[-1][-1] >> node
        
    return root


text=  """
# Appendices

The appendix begins with an epigraph by Pardot Kynes in which he considers the kind of existence available when humans increase in number in a finite environment.

## Appendix I: The Ecology of Dune.
This appendix details “the ecology of Dune.” It is heavily focused on the story of Pardot Kynes, Arrakis's first planetologist.

## Appendix II: The Religion of Dune.
Before the coming of [[Muad'Dib]], the Fremen of Arrakis practiced a religion whose roots in the Maometh Saari are there for any scholar to see. Many have traced the extensive borrowings from other religions. The most common example is the Hymn to Water, a direct copy from the Orange Catholic Liturgical Manual, calling for rain clouds which Arrakis had never seen. But there are more profound points of accord between the Kitab al-Ibar of the Fremen and the teachings of Bible, Ilm, and Fiqh.

## Appendix III: Report on Bene Gesserit Motives and Purposes.
This appendix details a “report on Bene Gesserit motives and purpose.”
The narrator introduces it by noting that Lady Jessica commissioned the report directly after the “Arrakis Affair.” 

### Narratives
The document is noted as being extremely honest in tone.

## Appendix IV: The Almanak eb-Ashraf (Selected Excerpts of the Noble Houses)
This appendix details selected excerpts about the noble Houses of Dune. The first entry discusses the Padishah Emperor Shaddam IV of House Corrino. His rule is most significant for the “Arrakis Revolt,” which historians ascribe to his poor court politics. 

# Terminology of the Imperium

Hello there

## Another One
asda
# """

root = buildTree(text)

print_tree(root)