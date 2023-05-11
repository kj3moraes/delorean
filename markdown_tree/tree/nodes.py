class TextLeaf:
    
    def __init__(self, text:str):
        self.text = text
        
    def __repr__(self):
        return self.text
    
    def __str__(self):
        return self.text
    

class HeaderNode:
    
    def __init__(self, header:str, depth:int):
        self.header = header
        self.depth = depth
        self.children = []
        
    def __repr__(self):
        return self.header
    
    def __getitem__(self, index:int):
        return self.children[index]
    
    def add_child(self, child):
        self.children.append(child)
        