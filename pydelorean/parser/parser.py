from treelib import Tree
from .utils import *

class Parser:
    
    def __init__(self, document_name:str, text:str):
        self.document_name = document_name
        self.text = text
        
    def parse(self) -> Tree:
        pass

   
class MarkdownParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Tree:
        HEADER_PATTERN = r"^(#+\s+)(.*)"
        
        tree = buildTree(self.text, self.document_name, header_pattern=HEADER_PATTERN)
        return tree
        

class RestructuredParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Tree:
        HEADER_PATTERN = r'^(\S.*)\n[=~`\'^"-]+$'
        
        tree = buildTree(self.text, self.document_name, header_pattern=HEADER_PATTERN)
        return tree
        

class TextParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Tree:
        pass


class YAMLParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Tree:
        pass


class JSONParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Tree:
        pass
    

class XMLParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Tree:
        pass
    
