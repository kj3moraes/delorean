from .node import HeaderNode


class Forest:
    
    def __init__(self, root:HeaderNode, documentName:str="[document]", metadata:dict=None):
        self.documentName = documentName
        self.metadata = metadata
        self.root = root
        
    # TODO: Implement __str__ and __len__ methods
    # FIGUREOUT: What other methods should this base class have ?


class MarkdownForest:
    
    # TODO: Make this a subclass of Forest
    def __init__(self, root:HeaderNode, documentName:str="[document]", metadata:dict=None):
        self.documentName = documentName
        self.metadata = metadata
        self.root = root

        # TODO: Implement a method to count the number of nodes in the tree
        
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
    

# FIGUREOUT: Do we really need a forest for each of the supported formats ?
class RestructuredForest:
    pass


class AsciidocForest:
    pass


class YamlForest:
    pass


class JSONForest:
    pass
