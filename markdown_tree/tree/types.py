class Node:
    
    def __init__(self, parent=None):
        self.parent = parent
           
    def __str__(self):
        return f"{self.__class__.__name__}()"


class TextNode(Node):
    
    FRACTION_PRINTABLE = 0.5
    
    def __init__(self, text:str, parent=None):
        self.text = text
        self.parent = parent
        
    def __getitem__(self, index:int):
        return self.text[index]
           
    def __str__(self):
        return self.text[0:min(10, int(self.FRACTION_PRINTABLE * len(self.text)))] + " ..."
    
    def get_parent(self):
        return self.parent


class HeaderNode(Node):
    
    def __init__(self, header:str, headerNumber:int=1, parent:Node=None):
        self.header = header
        self.headerNumber = headerNumber
        self.parent = parent
        self.children = []
        
    def __str__(self):
        return f"(h{self.headerNumber}) {self.header}"
    
    def __getitem__(self, index:int):
        return self.children[index]
    
    def get_parent(self):
        return self.parent
    
    def add_child(self, child:Node):
        self.children.append(child)
        
class MarkdownTree:
    
    def __init__(self, root:Node):
        self.root = root
        self.count = 0
        self.headerCount = 0
        self.wordCount = 0
        
    def __str__(self):
        # Helper function to print the tree
        def printTree(root:Node, markerStr="+- ", levelMarkers=[]):
            returnStr = ""
            emptyStr = " " * len(markerStr)
            connectionStr = "|" + emptyStr[:-1]
            level = len(levelMarkers)
            mapper = lambda draw: connectionStr if draw else emptyStr
            markers = "".join(map(mapper, levelMarkers[:-1]))
            markers += markerStr if level > 0 else ""
            returnStr += f"{markers}{root}\n"
            
            # Recurse on children if they exist
            if isinstance(root, HeaderNode):
                for i, child in enumerate(root.children):
                    isLast = i == len(root.children) - 1
                    returnStr += printTree(child, markerStr, [*levelMarkers, not isLast])
            return returnStr
        
        return printTree(self.root)
        
    def get_root(self):
        return self.root
    
class MarkdownForest:
    
    def __init__(self, documentName:str="[document]"):
        self.documentName = documentName
        self.trees = []
        self.treeCount = 0
        
    def __str__(self):
        return f"{self.documentName}\n".join(map(str, self.trees))
    
    def __getitem__(self, index:int):
        return self.trees[index]
    
    def __len__(self):
        return self.treeCount
    
    def add_tree(self, tree:MarkdownTree):
        self.trees.append(tree)
        self.treeCount += 1
    