
class Node:
    
    def __init__(self):
        pass
                   
    def __str__(self):
        return f"{self.__class__.__name__}()"


class TextNode(Node):
    
    FRACTION_PRINTABLE = 0.5
    
    def __init__(self, text:str, parent:Node=None):
        self.parent = parent
        self.text = text
        
    def __getitem__(self, index:int):
        if index < 0 or index >= len(self.text):
            raise IndexError("Index out of bounds")
        return self.text[index]
           
    def __str__(self):
        return self.text

    def __repr__(self) -> str:
        return "(Text) " + self.text[0:min(10, int(self.FRACTION_PRINTABLE * len(self.text)))] + " ..."
    
    def get_corpus(self) -> str:
        return self.text
    
    def set_corpus(self, corpus:str) -> None:
        self.text = corpus

class HeaderNode(Node):
    
    def __init__(self, header:str, headerNumber:int=1, parent:Node=None):
        self.parent = parent
        self.header = header
        self.corpus = "#" * headerNumber + " " + header + "\n\n"
        self.headerNumber = headerNumber
        self.children = []
        
    def __str__(self):
        return self.header
    
    def __repr__(self):
        return f"(h{self.headerNumber}) {self.header}"
    
    def __len__(self):
        return len(self.children)
    
    def __iter__(self):
        for elem in self.children:
            yield elem
    
    def __getitem__(self, index:int) -> Node:
        return self.children[index]
    
    def set_corpus(self, corpus:str) -> None:
        self.corpus = corpus
    
    def get_corpus(self) -> str:
        return self.corpus
    
    def append_corpus(self, corpus:str) -> None:
        self.corpus += corpus
    
    def get_header_level(self) -> int:
        return self.headerNumber
    
    def add_child(self, child:Node) -> None:
        self.children.append(child)
        
class MarkdownTree:
    
    def __init__(self, root:Node):
        self.root = root
        self.words = root.get_corpus().split()
        self.wordCount = len(self.words)
        self.vocab = set(self.words)
        self.vocabSize = len(self.vocab)
        
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
    
    def __init__(self, documentName:str="[document]", metadata:dict=None):
        self.documentName = documentName
        self.metadata = metadata
        self.trees = []
        self.treeCount   = 0
        self.backlinks = []
        self.tags = []
        
    def __str__(self):
        return f"[{self.documentName}]\n" + "\n".join(map(str, self.trees))
    
    def __getitem__(self, index:int):
        if index < 0 or index >= self.treeCount:
            raise IndexError("Index out of bounds")
        return self.trees[index]
    
    def __len__(self):
        return self.treeCount

    def get_metadata(self):
        return self.metadata

    def add_tree(self, tree:MarkdownTree):
        self.trees.append(tree)
        self.treeCount += 1
    
    def add_backlink(self, backlink:str):
        self.backlinks.append(backlink)
    
    def get_backlinks(self):
        return self.backlinks
    
    def add_tag(self, tag:str):
        self.tags.append(tag)
        
    def get_tags(self):
        return self.tags

