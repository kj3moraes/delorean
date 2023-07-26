"""
    Copyright 2023 Keane Moraes

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

from bigtree import Node

# TODO: Add all the documentation and convert to snake case soon.


class TextNode(Node):
    
    FRACTION_PRINTABLE = 0.25   
    
    def __init__(self, name:str, text:str, **kwargs):
        self.text = text
        self.corpus = text
        super().__init__(name=name, **kwargs)
        
        
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
        super().__init__(name=header, **kwargs)
        
    def __str__(self):
        return self.header
    
    def __repr__(self):
        return f"(h{self._header_level}) {self.header}"
    
    def __and__(self, other):
        self.corpus += "\n" + other.corpus
           

        
