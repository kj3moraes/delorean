from .utils import *

class Parser:
    
    def __init__(self, document_name:str, text:str):
        self.document_name = document_name
        self.text = text
        
    def parse(self) -> Node:
        pass

   
class MarkdownParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Node:
        HEADER_PATTERN = r"^(#+\s+)(.*)"
        
        tree = build_tree(self.text, document_name=self.document_name, header_pattern=HEADER_PATTERN)
        return tree
        

class RestructuredParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Node:
        HEADER_PATTERN = r"^(=+|-+|`+|'+|\^+|\*+|\.+|~+|\++)\s+(.+)\s+\1$"
        
        tree = build_tree(self.text, document_name=self.document_name, header_pattern=HEADER_PATTERN)
        return tree
   

class AsciiDocParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Node:
        pass     


class TextParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Node:
        pass


class YAMLParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Node:
        pass


class JSONParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Node:
        pass
    

class XMLParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Node:
        pass
    
