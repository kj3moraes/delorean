"""_summary_

"""

from bigtree import BaseNode, Node

# TODO: Add all the documentation and convert to snake case soon.


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
    
    def __init__(self, name:str, text:str, **kwargs):
        self.text = text
        super().__init__(name, **kwargs)
        
        
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

class HeaderNode(Node):
    """_summary_

    Args:
        Node (_type_): _description_
    """
    
    def __init__(self, name:str, header:str, headerNumber:int, **kwargs):
        self.header = header
        self.headerNumber = headerNumber
        self.name = header
        self.corpus = []
        super().__init__(name, **kwargs)
        
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




