from .node import HeaderNode


class Forest:
    
    def __init__(self, root:HeaderNode, document_name:str="[document]"):
        self.document_name = document_name
        self.root = root
        self.num_trees = len(root.children)
        # TODO: Implement a method to count the number of nodes in the tree
    
    def __str__(self):
        return str(self.root)
    
    def __len__(self):
        return self.num_trees
    
    @property
    def name(self):
        return self.document_name
    
    @name.setter 
    def name(self, document_name:str):
        self.document_name = document_name    
    
    def set_root(self, root:HeaderNode):
        self.root = root
    
    # TODO: Implement __str__ and __len__ methods
    # FIGUREOUT: What other methods should this base class have ?


class MarkdownForest(Forest):
    
    # TODO: Make this a subclass of Forest
    def __init__(self, root:HeaderNode, document_name:str="[document]", metadata:dict=None):
        super().__init__(root, document_name)
        self.metadata = metadata
        self.backlinks = []
        self.tags = []

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
    

class RestructuredForest(Forest):
    pass


class AsciiDocForest(Forest):
    
    def __init__(self, root:HeaderNode, document_name:str="[document]", document_type:str="article"):
        super().__init__(root, document_name)
        self.document_type = document_type
    
    def get_document_type(self):
        return self.document_type


class TextForest(Forest):
    pass    

class YAMLForest(Forest):
    pass


class JSONForest:
    pass

class XMLForest(Forest):
    pass