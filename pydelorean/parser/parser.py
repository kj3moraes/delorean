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
        build_corpus(tree)
        return tree
        

class RestructuredParser(Parser):
    
    def __init__(self, document_name:str, text:str):
        super().__init__(document_name, text)
        
    def parse(self) -> Node:
        HEADER_PATTERN = r"^(=+|-+|`+|'+|\^+|\*+|\.+|~+|\++)\s+(.+)\s+\1$"
        
        tree = build_tree(self.text, document_name=self.document_name, header_pattern=HEADER_PATTERN)
        build_corpus(tree)
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
    
