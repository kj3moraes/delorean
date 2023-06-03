import frontmatter 
import re
from bs4 import BeautifulSoup
from markdown import markdown
from tree.types import *
from treebuild import TOC

# ==================================================================================================
#                                           TREEIFY
# ==================================================================================================


def generateRootNodeFromContents(currTree:TOC, parent:Node=None) -> Node:
    """ Function to generate the tree of a specific header's section.
    """    
    # BASE CASE: If there is no depth, then it is just a paragraph
    if currTree.getHeadingLevel(currTree.source) == None:
        return TextNode(currTree.source.string, parent=parent)
    
    # Get the current header of the tree
    headerText = currTree.source.string
    currentHeaderLevel = currTree.getHeadingLevel(currTree.source)
    rootNode = HeaderNode(headerText, headerNumber=currentHeaderLevel, parent=parent)

    for child in currTree.branches:
        if child.getHeadingLevel(child.source) == None:
            resultNode = TextNode(child.source.string, parent=rootNode)
        else:
            resultNode = generateRootNodeFromContents(child, parent=rootNode)
        
        corpus = resultNode.get_corpus()
        rootNode.add_child(resultNode)
        rootNode.append_corpus(corpus)
                
    return rootNode    

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

def mdtreeify(name:str, md:str, *args, **kwargs) -> MarkdownForest:
    """
    Converts markdown file to a MarkdownForest
    """
    
    meta, cont = find_metadata(md)
    
    backlinks = find_backlinks(cont)
    tags = find_tags(cont)
    returnForest = MarkdownForest(name, metadata=meta)
    
    for backlink in backlinks:
        returnForest.add_backlink(backlink)
    for tag in tags:
        returnForest.add_tag(tag)
    
    html = markdown.markdown(cont)
    toc =  BeautifulSoup(html, 'html.parser')
    for tree in toc.branches:
        root = generateRootNodeFromContents(tree)
        returnForest.add_tree(MarkdownTree(root))
    
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

def mdtextify(forest:MarkdownForest, *args, **kwargs) -> str:
    
    finalText = convertDictToMetadata(forest.metadata)
    for i, tree in enumerate(forest):
        finalText += convertRootToText(tree.get_root())
    return finalText

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

text = """
# A basic overview of Zettel and Zettelkasten

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

### Inheritance 

A basic concept in object oriented programming is _inheritance._ This describes the way _classes_ inherit  properties of other classes - where instances of classes are _objects_ that in a sense are parts of a machine that you materialize from your _library of classes_ when you run a piece of computer code. A good programmer who's building a _library of classes_ that they use in a project should structure their library so that any class that shares properties with another class _inherits_ those properties automatically from that class or a class that describes a more general object rather than having those properties repeatedly redefined in what could end up being a slightly different ways that add confusion or inconsistencies to the structure of the class library. This leads to an emergent structure within a class library called a _class hierarchy._

I see some parallels between this site and a class library. As I've expanded this site I've become more aware of the ways in which more specialized notes inherit aspects of more generalized notes - in order to reflect this I've, over time, become more careful about never repeating information and using block references to other notes as a much as I can in order reflect inheritance. This is one way in which I'm able to filter out what's actually the important point to learn from a particular note, rather than letting myself get bogged down in the details that surround it. What I find particularly compelling is how I may be able to use this approach structure worked examples of solutions to specific [physics problems](Thoughts%20on%20What%20this%20Site%20is.md#The%20importance%20of%20seeing%20underlying%20mechanisms). For example, I may be describing the model for a _quantum harmonic oscillator_. In doing so, I'm forced to reference concepts like _Hamiltonian_ or the _classical harmonic oscillator._ In trying to define what exactly a quantum harmonic oscillator is, I find that it _inherits_ some basic properties from classical oscillators, which I may then invoke in a more specific quantum mechanical problem (such as a particle trapped in a particular potential) via a reference to only the quantum oscillator. In solving more complicated problems I may invoke, often using [block references](The%20Quantum%20Well%20Style%20Guide.md#Block%20references), many different notes that, if this were a coding project, would form a class sub-library that I draw from for specific applications. This makes me more aware of exactly what tools I need for every problem and provides me with a new found clarity in my problem solving approach. 

### Detailed style guide I follow

While this page describes my general paradigm and some practices, I aim to create an even more detailed style guide [here.](The%20Quantum%20Well%20Style%20Guide.md)

## Reasons I was drawn to _Zettelkasten_

When approaching a complicated topic, information is typically presented in the form of a wall of text - a wall full of connective statements and references to other bits of information that were previously mentioned or the reader is expected to know already. It should come as no surprise that in highly technical fields, such as quantum optics, or mathematical analysis, one's expected to just know a lot of things already before picking up the more useful textbooks out there. And the farther one gets into a topic, the more one relies on knowledge drawn from multiple sources. In order to relate topics to prerequisite knowledge as well as quickly expand on particular topics, I found a networked approach provided by the _Zettelkasten_ method to be easiest to organize. This becomes so much easier using software - no need to actually physically move cards around or worry about indexing them with a numbering system, as would be done in a physical _Zettelkasten_.

### Parallels to animal brains

The exact ways memory is stored in a brain is beyond the scope of this text - however I can say with confidence that I know that brains are also networked structures, and as I have a brain, I'm painfully aware that I don't have a filing cabinet in my head or stacks of textbooks I can reference specific pages of in order to extract the exact concept or formula I need at any given point. Rather, it would appear that our thoughts and memories are a matrix of fleeting ideas triggered by associations and that with each instantiation, we alter a memory slightly. The seemingly disordered way in which information actually seems to connect to other bits of information in our minds and possibly outside of our minds becomes apparent when I map out the [connectome](Welcome%20to%20The%20Quantum%20Well!.md#The%20Graph%20View) of all the items on this site. Roughly speaking, under this paradigm, every physics or math problem is a _node_ and every step towards a solution is a _connection._

By restricting myself to atomic notes and focusing on associations between ideas, my note taking strategy and the way I want to experiment in presenting information structures a systematized referenced library around the constraints of our animal brains. 

---

_This is one of several blog-post style pages that's not part of the [indexed notes](Welcome%20to%20The%20Quantum%20Well!.md#Indices) that constitute what I consider to be the core content to this site._ 

# TRhis asd a text

"""

toc =  TOC.fromMarkdown(text)
print(toc.source)
root = generateRootNodeFromContents(toc)