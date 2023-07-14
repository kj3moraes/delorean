from pydelorean.tree.node import *
from pydelorean import treeify

def get_progressive_expansion(node, **kwargs) -> list:
    
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


# text = """
# ---
# author: Keane Moraes
# id: 1
# tags:
# - dune
# - ecology
# - fremen
# - religion
# - desert
# ---

# # Appendices

# The appendix begins with an epigraph by Pardot Kynes in which he considers the kind of existence available when humans increase in number in a finite environment.

# ## Appendix I: The Ecology of Dune.
# This appendix details “the ecology of Dune.” It is heavily focused on the story of Pardot Kynes, Arrakis's first planetologist.

# ## Appendix II: The Religion of Dune.
# Before the coming of [[Muad'Dib]], the Fremen of Arrakis practiced a religion whose roots in the Maometh Saari are there for any scholar to see.

# ## Appendix III: Report on Bene Gesserit Motives and Purposes.
# This appendix details a “report on Bene Gesserit motives and purpose.”
# The narrator introduces it by noting that Lady Jessica commissioned the report directly after the “Arrakis Affair.” 

# ### Narratives
# The document is noted as being extremely honest in tone.

# ## Appendix IV: The Almanak eb-Ashraf (Selected Excerpts of the Noble Houses)
# This appendix details selected excerpts about the noble Houses of Dune. The first entry discusses the Padishah Emperor Shaddam IV of House Corrino. His rule is most significant for the “Arrakis Revolt,” which historians ascribe to his poor court politics. 

# # Terminology of the Imperium

# Hello there

# ## Another One

# asdfas
# """

# forest = treeify("dune_appendices.md", text)

# root = forest.root
# header1 = root.children[0]

# ans = get_progressive_expansion(root, append=True)

# for i in ans:
#     print(i)
#     print("==================================")