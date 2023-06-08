import frontmatter 
import re
from bs4 import BeautifulSoup
from markdown import markdown
from tree.types import *
from treelib import Tree, Node

# ==================================================================================================
#                                           TREEIFY
# ==================================================================================================

def buildTree(inputText:str, tree:Tree, root_id) :
    
    assert isinstance(inputText, str), "inputText must be a string"
    # assert inputText != "", "inputText cannot be an empty string"
    if inputText == "":
        return []

    HEADER_PATTERN = r'^#+\s+(.*)$'
    
    matches = re.finditer(HEADER_PATTERN, inputText, re.MULTILINE)
        
    # Get all the indices of the headers
    indices = [(match.start(), match.end()) for match in matches]
    # indices.sort(key=lambda x: x[0])
    
    # BASE CASE ===
    # Check if it is only text (since there are no header indices)
    if len(indices) == 0:
        # returnNode = Node(tag=inputText[0:10], data=inputText)
        # returnNode.predecessor = root_id
        tree.create_node(inputText, inputText, parent=root_id)
        return
    
    # IS THERE TEXT BEFORE THE FIRST HEADER?
    if indices[0][0] != 0:
        textBefore = inputText[0:indices[0][0]]
        # textNode = Node(tag=textBefore[0:10], data=textBefore)
        # textNode.predecessor = root_id
        tree.create_node(textBefore, textBefore, parent=root_id)
    
    # FIXME: USE THE STACK STRUCTURE THAT JAIMIL SAID TO USE
    
    stack = []
    
    # Get information on the starting header that will be searched from.
    currHeader = indices[0]
    currHeaderText = inputText[currHeader[0]:currHeader[1]]
    currHeaderLevel = len(currHeaderText) - len(currHeaderText.replace("#", ""))
    
    # Create the header node with the current header.
    node = tree.create_node(currHeaderText, parent=root_id)
    # currHeaderNode = Node(tag=currHeaderText, data=(currHeaderText, currHeader, currHeaderLevel))
    # currHeaderNode.predecessor = root_id
    
    # Add the node to the stack
    stack.append((currHeaderLevel, currHeader, node.identifier))

    for i in range(1, len(indices)):
        currHeader = indices[i]
        currHeaderText = inputText[currHeader[0]:currHeader[1]]
        currHeaderLevel = len(currHeaderText) - len(currHeaderText.replace("#", ""))
        # currHeaderNode = Node(tag=currHeaderText, data=(currHeaderText, currHeader, currHeaderLevel))
        lastHeader = stack[-1]
        # CASE 1: If the current header level is greater than the starting header level then keep going.
        if currHeaderLevel > lastHeader[0]:
            # Extract the text between the current header and the previous header
            textBetween = inputText[lastHeader[1][1]:currHeader[0]].strip()
            if textBetween != "":
                tree.create_node(tag=textBetween[0:min(10, len(textBetween))], data=textBetween, parent=lastHeader[-1])
            # Node(tag=textBetween[0:10], data=textBetween)
            # textNode.predecessor = stack[-1].identifier
            # stack[-1].update_successors(textNode.identifier)
            
            # Add the current header as a node to the stack and its parent is the previous header
            # currHeaderNode.predecessor = stack[-1].identifier
            # stack[-1].update_successors(currHeaderNode.identifier)
            node = tree.create_node(tag=currHeaderText, parent=lastHeader[-1])
            stack.append((currHeaderLevel, currHeader, node.identifier))
            
        # CASE 2: If the current header level is less than or equal to the starting header level then we need to create a new tree.
        elif currHeaderLevel <= lastHeader[0]:
            textBetween = inputText[lastHeader[1][1]:currHeader[0]].strip()
            if textBetween != "":
                tree.create_node(tag=textBetween[0:min(10, len(textBetween))], data=textBetween, parent=lastHeader[-1])
            
            # Pop off until you get to the node with a lower level than the current header level
            while len(stack) > 0: 
                if stack[-1][0] >= currHeaderLevel:
                    stack.pop()
                else:
                    break
            
            if len(stack) == 0:
                node = tree.create_node(currHeaderText, parent=root_id)
            else:
                node = tree.create_node(currHeaderText, parent=stack[-1][-1])
            stack.append((currHeaderLevel, currHeader, node.identifier))
                
                
    # Check if there is any text after the last header
    if indices[-1][1] != len(inputText):
        textEnd = inputText[indices[-1][1]:].strip()
        tree.create_node(tag=textEnd[:min(10, len(textEnd))], data=textEnd, parent=stack[-1][-1])
    

    # if not foundLower:
    #     textBetween = inputText[startHeader[1]:].strip()
    #     buildTree(textBetween, parent_id=startHeaderNode.identifier)
    #     return returnNodes
            
    

def findBacklinks(input_text:str) -> list:
    """ 
    Function to find all backlinks in a given text.
    """
    
    backlinks = []

    # Regular expression pattern to match backlinks
    pattern = r'\[\[(.*?)\]\]'
    backlinks = re.findall(pattern, input_text)
    return backlinks

def findTags(input_text:str) -> list:
    """
    Function to find all tags in a given text.
    """
    
    tags = []

    # Regular expression pattern to match backlinks
    pattern = r'#([a-zA-Z0-9_]+)'
    tags = re.findall(pattern, input_text)
    return tags

def findMetadata(input_text:str):
    post = frontmatter.loads(input_text)
    return post.metadata, post.content

def mdtreeify(name:str, md:str, *args, **kwargs) -> Tree:
    """
    Converts markdown file to a MarkdownForest
    """
    
    meta, cont = findMetadata(md)
    
    backlinks = findBacklinks(cont)
    tags = findTags(cont)
    tree = Tree()
    tree.create_node(name, "root")
    buildTree(cont, tree, "root")
    returnForest = MarkdownForest(tree, name, metadata=meta)
    
    for backlink in backlinks:
        returnForest.add_backlink(backlink)
    for tag in tags:
        returnForest.add_tag(tag)

    return returnForest


# ==================================================================================================
#                                           TEXTIFY
# ==================================================================================================

    
def convertRootToText(rootNode: Node) -> str:
    
    # BASE CASE: We just have text node.
    if isinstance(rootNode, TextNode):
        return repr(rootNode) + "\n"
    
    # For the header node
    headerLevel = rootNode.get_header_level()
    returnString = '#'*headerLevel + " " + str(rootNode) + "\n"
    for i, child in enumerate(rootNode):
        returnString += convertRootToText(child)
    
    return returnString    
        
def convertDictToMetadata(metadata:dict) -> str:
    yaml = "---\n"
    for key, value in metadata.items():
        if isinstance(value, list):
            yaml += f"{key}: \n"
            for elem in value:
                yaml += f"  - {elem}\n"
            continue
        yaml += f"{key}: {value}\n"
    yaml += "---\n"
    return yaml

# def mdtextify(forest:MarkdownForest, *args, **kwargs) -> str:
    
#     finalText = convertDictToMetadata(forest.metadata)
#     for i, tree in enumerate(forest):
#         finalText += convertRootToText(tree.get_root())
#     return finalText

def parse_html_to_tree(html):
    soup = BeautifulSoup(html, 'html.parser')
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    def build_tree(node):
        result = []
        for sibling in node.next_siblings:
            if sibling.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                break
            if sibling.name == 'p':
                result.append(sibling.get_text())
        return result

    forest = {}
    for header in headers:
        header_text = header.get_text()
        forest[header_text] = build_tree(header)

    return forest

test_text = """
# A basic overview of _Zettel_ and _Zettelkasten_

The main idea behind any system based on atomic notes is that one should restrict ideas to single sheets of index card paper - thus collecting stacks of index cards containing important ideas. Atomizing ideas into small chunks simply makes them easier to remember. However, more importantly, it is easier to turn them into pieces that fit into a living body of information we refer to as a _Zettelkasten_. 

In order to create a proper Zettelkasten each card should be associated with meta-data that determines its place relative to other cards in that slipbox, hence forming a networked structure and clusters of cards that form categories as the number of cards grows. The beauty in this is that these structures and categories emerge naturally over time, and force the user to periodically review what they have already in order to contextualize new knowledge. Effectively, this means that your Zettelkasten is a _partner of communication_ [as described by Luhmann](http://luhmann.surge.sh/communicating-with-slip-boxes) since, in comparison to planned structures, emergent structures are able to offer surprises (that is, insights that wouldn't have otherwise been expected) to anyone who interfaces with them. 

What typically happens instead is that over the years we take notes in notebooks, then when we put away these notes, we often never read them again. One can hope that we can keep remembering what we learn from simply writing it down, but that's not usually the case. If we repeatedly use the same bits of information, that information will stick, but there's no guarantee that we can draw from the much broader body of ideas we've encountered if our old notes are left to collect dust. _Zettelkästen_, on the other hand, are in my view a remedy to this, since, they are modular and they encourage users to consider new notes as existing within a context created by older notes. 

## My own implementation and why it works for me

I found this framework useful for many reasons. However, I develop my own specific [format and stylistic conventions](The%20Quantum%20Well%20Style%20Guide.md) that suit me personally - and ultimately this is for _me._ I am also constantly adjusting my organizational scheme to reflect my shifting needs. I will continue to update this page as well as the [formal style guide](The%20Quantum%20Well%20Style%20Guide.md) as I discover new strategies and incorporate additional paradigms. 

I refer to entries I make on this site as _pages_ instead of _notes_, or _zettel_, whereas subsections in those pages will approximate _atomic notes_ or _zettel_. It will often also be the case that I summarize a topic within a nested sub-section, and then have that subsection linked to a proper page going into the full detail of that subtopic. Whether I follow specific Zettelkasten conventions isn't as important to me as the core ethos as [described by Luhmann.](http://luhmann.surge.sh/communicating-with-slip-boxes) What this means is I aim to [generate insights](Thoughts%20on%20What%20this%20Site%20is.md#Solving%20problems%20more%20efficiently) by using this system as a partner of communication. ^32f125

### Presenting information 

I don't just note information, I want to _present it_ as well. In a typical _Zettelkasten_ polish is not a concern and in fact can interfere with its efficiency in quickly collect information. However, from my experience, presentation quality has been tied to how well I understand a topic. Thus, by explaining things as carefully as possible, I can feel confident in my own understanding. 

Many pages on here may seem like rough drafts, or scattered formulas regardless, but with every revisit of every page, I add polish, and with that, a more precise understanding. 

### The role of indices

Here we consider the role of [indices.](Welcome%20to%20The%20Quantum%20Well!.md#Indices) In the simplest terms, they are hubs to which many related notes link to. Indices add another organizational layer beyond simple links between pages. With hyperlinks I can more easily define any number of indices in order to connect topics in ways I see fit for different purposes. 

### The role of folders

Folders on a computer are actually where my pages are stored. However the use of more than one folder and nested sub-folders in a Zettelkasten is often discouraged or at least seen as something that should be used only rarely since they are seen as overly rigid for something a dynamic as a Zettelkasten [(see one discussion on the matter here).](https://publish.obsidian.md/lyt-kit/Umami/In+what+ways+can+we+form+useful+relationships+between+notesI) I don't agree with folder detractors. As a complement to [indices](Knowledge%20Management.md#The%20role%20of%20indices), I also have a hierarchy of folders. This is especially important as I approach and eventually surpass 1000 notes and items. I also have a folder for [uncategorized notes](Welcome%20to%20The%20Quantum%20Well!.md#Uncategorized%20Notes) for some very rough drafts and cases for which I don't know where to put something. In some cases it can be slightly arbitrary in what folder something goes. Thus, the only rules I enforce with regards to folders are: 

1. Every folder corresponds to and contains _one_ [Index](Welcome%20to%20The%20Quantum%20Well!.md#Indices)
2. Every item in a given folder must be linked to the index of that folder. 

The extent to which folders may be overly rigid is circumvented by the fact that I have the option to place a link to a note in multiple indices as well as a [tagging system](Knowledge%20Management.md#The%20role%20of%20tags) that creates a more flexible way to categorize topics. 

### The role of tags

Tags provide yet another layer of metadata beyond links to other pages and links to indices to include on each page. Tags are a way to provide "loose" links between pages by defining overarching categories that may be either more specific or more general than the categorizations defined by [indices.](Knowledge%20Management.md#The%20role%20of%20indices) For example, I might not want every differential equation to link back to the page that gives the general concept of differential equations or to every other differential equation. However, I may want some link to a tag that also can be found under other differential equations in order to reveal a broad commonality. Tags are also a simple way to express how some pages fall under more than one category. e.g. I'd consider some of my pages to be purely mathematical while also being topics in physics. Thus something may be tagged as being both in common with pages that are categorized in a subfolder of quantum mechanics and a subfolder of my mathematical foundations pages. I'm also particularly fond of nested tags that allow me to condense the information given by the tags into fewer tags that are easier to keep track of despite their unruly lengths. 

---

_This is one of several blog-post style pages that's not part of the [indexed notes](Welcome%20to%20The%20Quantum%20Well!.md#Indices) that constitute what I consider to be the core content to this site._ 

# TRhis asd a text

"""

basic_text = """
# This is a title
asdasd
""".strip()

tree = mdtreeify("testing", test_text)
print(tree)