class Node:
    
    def __init__(self, parent=None):
        self.parent = parent
        
    def __repr__(self):
        return f"{self.__class__.__name__}()"
    
    def __str__(self):
        return f"{self.__class__.__name__}()"


class TextNode(Node):
    
    def __init__(self, text:str, parent=None):
        self.text = text
        self.parent = parent
        
    def __repr__(self):
        return self.text[0:min(10, 0.1 * len(self.text))]
    
    def __str__(self):
        return self.text
    
    def get_parent(self):
        return self.parent
    
def printTree(root, markerStr="+- ", levelMarkers=[]):
        emptyStr = " " * len(markerStr)
        connectionStr = "|" + emptyStr[:-1]
        level = len(levelMarkers)
        mapper = lambda draw: connectionStr if draw else emptyStr
        markers = "".join(map(mapper, levelMarkers[:-1]))
        markers += markerStr if level > 0 else ""
        print(f"{markers}{root}")
        if isinstance(root, HeaderNode):
            for i, child in enumerate(root.children):
                isLast = i == len(root.children) - 1
                printTree(child, markerStr, [*levelMarkers, not isLast])  

class HeaderNode(Node):
    
    def __init__(self, header:str, parent=None):
        self.header = header
        self.parent = parent
        self.children = []
        
    def __repr__(self):
        return self.header
    
    def __str__(self):
        return self.header
    
    def __getitem__(self, index:int):
        return self.children[index]
    
    def get_parent(self):
        return self.parent
    
    def add_child(self, child):
        self.children.append(child)
        
class MarkdownTree:
    
    def __init__(self, root:Node):
        self.root = root
        self.count = 0
        self.headerCount = 0
        self.wordCount = 0
        
        
        
original_tree = MarkdownTree(HeaderNode("root"))
original_tree.root.add_child(HeaderNode("header1", original_tree.root))
original_tree.root[0].add_child(HeaderNode("header3", original_tree.root[0]))
original_tree.root.add_child(HeaderNode("header2", original_tree.root))
original_tree.root.add_child(TextNode("The work is now done for this class", original_tree.root))
printTree(original_tree.root)