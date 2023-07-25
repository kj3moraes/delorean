"""_summary_

"""

from bigtree import Node

# TODO: Add all the documentation and convert to snake case soon.


class TextNode(Node):
    
    FRACTION_PRINTABLE = 0.25   
    
    def __init__(self, name:str, text:str, **kwargs):
        self.text = text
        self.corpus = text
        super().__init__(name, **kwargs)
        
        
    def __getitem__(self, index:int):
        if index < 0 or index >= len(self.text):
            raise IndexError("Index out of bounds")
        return self.text[index]
           
    def __str__(self):
        return self.text[0:min(10, int(self.FRACTION_PRINTABLE * len(self.text)))] + " ..."

    def __repr__(self) -> str:
        return "(Text) " + self.text[0:min(10, int(self.FRACTION_PRINTABLE * len(self.text)))] + " ..."
    

class HeaderNode(Node):
    
    def __init__(self, header:str, headerNumber:int, **kwargs):
        self.header = header
        self.header_level = headerNumber
        self.corpus = header + "\n"
        super().__init__(header, **kwargs)
        
    def __str__(self):
        return self.header
    
    def __repr__(self):
        return f"(h{self._header_level}) {self.header}"
    
    def __and__(self, other):
        self.corpus += "\n" + other.corpus
           

        
