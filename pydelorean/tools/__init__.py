from bigtree import Node
from pydelorean.tree.types import HeaderNode, TextNode
from pydelorean import treeify

def get_progressive_expansion(node, **kwargs) -> list:
    
    # BASE CASE: TextNode
    if isinstance(node, TextNode):
        return [(node.text, "")]
    
    header = node.header
    children = node.children
    returned_list = []
    final_corpus = ""
    for child in children:
        child_corpus = get_progressive_expansion(child)
        for child in child_corpus:
            text = child[0] + "\n" + child[1]
            returned_list.append((header, text))
            final_corpus += "\n" + text
    
    if 'append' in kwargs and kwargs['append']:
        returned_list.append((header, final_corpus))
    return returned_list
        
    
text = """
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
"""

# tree = treeify("appendices of dune", text)

# headerlist = get_progressive_expansion(tree.root.children[0], append=True)
# for pair in headerlist:
#     print(pair)
#     print("------------------")