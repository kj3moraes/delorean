from pydelorean.tree.node import TextNode

def get_progressive_expansion(node, **kwargs) -> list:
    
    # BASE CASE: TextNode
    if isinstance(node, TextNode):
        return [(node.text, "")]
    
    # BASE CASE: root node 
    if node.is_root:
        header = node.name
    else:
        header = node.header
    children = node.children
    returned_list = []
    final_corpus = ""
    for child in children:
        child_corpus = get_progressive_expansion(child)
        for child in child_corpus:
            text = child[0] + "\n" + child[1]
            returned_list.append((header, text))
            final_corpus += "\n" + text
    
    if 'append' in kwargs and kwargs['append']:
        returned_list.append((header, final_corpus))
    return returned_list
        
