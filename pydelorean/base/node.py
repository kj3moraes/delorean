"""_summary_

"""

from bigtree import Node

# TODO: Add all the documentation and convert to snake case soon.


class TextNode(Node):
    
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
    
    @property
    def corpus(self):
        return self._text
    
    @text.setter
    def text(self, text:str):
        self._text = text


class HeaderNode(Node):
    
    def __init__(self, header:str, headerNumber:int, **kwargs):
        self.header = header
        self._header_level = headerNumber
        self._corpus = []
        super().__init__(header, **kwargs)
        
    def __str__(self):
        return self.header
    
    def __repr__(self):
        return f"(h{self._header_level}) {self.header}"
    
    @property
    def header_level(self) -> int:
        return self._header_level
    
    @header_level.setter
    def header_level(self, headerNumber:int) -> None:
        self._header_level = headerNumber

    def __pow__(self, other):
        self._corpus.append(other)
        
    @property
    def corpus(self) -> str:
        final_text = self.header + "\n"
        for child in self._corpus:
            final_text += child.corpus + "\n"
        return final_text    

        
