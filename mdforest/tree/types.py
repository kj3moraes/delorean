"""_summary_

"""

from treelib import Tree

# TODO: Add all the documentation and convert to snake case soon.

class Node:
    """_summary_
    """
    
    def __init__(self):
        pass
                   
    def __str__(self):
        return f"{self.__class__.__name__}()"


class TextNode(Node):
    """_summary_

    Args:
        Node (_type_): _description_

    Raises:
        IndexError: _description_

    Returns:
        _type_: _description_
    """
    
    FRACTION_PRINTABLE = 0.25
    
    def __init__(self, text:str):
        self.text = text
        
    def __getitem__(self, index:int):
        if index < 0 or index >= len(self.text):
            raise IndexError("Index out of bounds")
        return self.text[index]
           
    def __str__(self):
        return self.text[0:min(10, int(self.FRACTION_PRINTABLE * len(self.text)))] + " ..."

    def __repr__(self) -> str:
        return "(Text) " + self.text[0:min(10, int(self.FRACTION_PRINTABLE * len(self.text)))] + " ..."
    
    @property
    def text(self):
        return self.text

class HeaderNode(Node):
    """_summary_

    Args:
        Node (_type_): _description_
    """
    
    def __init__(self, header:str, headerNumber:int, parentID):
        self.parentID = parentID
        self.header = header
        self.headerNumber = headerNumber
        self.corpus = []
        
    def __str__(self):
        return self.header
    
    def __repr__(self):
        return f"(h{self.headerNumber}) {self.header}"
        
    @property
    def corpus(self) -> str:
        return "\n".join(self.corpus)
    
    def append_corpus(self, corpus:str) -> None:
        self.corpus += corpus
        
    @property
    def headerLevel(self) -> int:
        return self.headerNumber


class MarkdownForest:
    
    def __init__(self, root:Tree, documentName:str="[document]", metadata:dict=None):
        self.documentName = documentName
        self.metadata = metadata
        self.root = root
        self.treeCount = len(root.children('root'))
        self.backlinks = []
        self.tags = []
        
    def __str__(self):
        return str(self.root)
    
    def __len__(self):
        return self.treeCount

    def add_root(self, root:Tree):
        self.root = root

    def get_metadata(self):
        return self.metadata
    
    def add_backlink(self, backlink:str):
        self.backlinks.append(backlink)
    
    def get_backlinks(self):
        return self.backlinks
    
    def add_tag(self, tag:str):
        self.tags.append(tag)
        
    def get_tags(self):
        return self.tags

