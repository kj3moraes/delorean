"""_summary_

"""

from bigtree import BaseNode

# TODO: Add all the documentation and convert to snake case soon.


class TextNode(BaseNode):
    """_summary_

    Args:
        Node (_type_): _description_

    Raises:
        IndexError: _description_

    Returns:
        _type_: _description_
    """
    
    FRACTION_PRINTABLE = 0.25
    
    def __init__(self, text:str, **kwargs):
        self.text = text
        super().__init__(**kwargs)
        
        
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
        return self._text
    
    @text.setter
    def text(self, text:str):
        self._text = text

class HeaderNode(BaseNode):
    """_summary_

    Args:
        Node (_type_): _description_
    """
    
    def __init__(self, header:str, headerNumber:int, **kwargs):
        self.header = header
        self.headerNumber = headerNumber
        self.name = header
        self.corpus = []
        super().__init__(**kwargs)
        
    def __str__(self):
        return self.header
    
    def __repr__(self):
        return f"(h{self.headerNumber}) {self.header}"
    
    @property
    def headerLevel(self) -> int:
        return self.headerNumber
    
    @headerLevel.setter
    def headerLevel(self, headerNumber:int) -> None:
        self._headerNumber = headerNumber
        
    def get_corpus(self) -> list:
        return self.corpus
    
    def add_to_corpus(self, text:str) -> None:
        self.corpus.append(text)


class MarkdownForest:
    
    def __init__(self, root:HeaderNode, documentName:str="[document]", metadata:dict=None):
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

    def add_root(self, root:HeaderNode):
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

