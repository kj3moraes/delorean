from treelib import Tree, Node
from pydelorean.tree.types import TextNode, HeaderNode

def get_progressive_expansion(tree:Tree, node_id, **kwargs) -> list:
    
    node = tree.get_node(node_id)
    
    # BASE CASE: TextNode
    if not isinstance(node.data, HeaderNode):
        return [node.data.text]
    
    header = node.data.header
    child_ids = tree.children(node_id)
    returned_list = []
    final_corpus = header
    for child_id in child_ids:
        child_corpus = get_progressive_expansion(tree, child_id.identifier)
        print("\n===THE CHILD CORPUS IS\n", child_corpus)
        for child in child_corpus:
            returned_list.append(header + "\n" + child)
            final_corpus += "\n" + child
    
    if 'append' in kwargs and kwargs['append']:
        returned_list.append(final_corpus)
    # print("===THE FINAL CORPUS IS\n", final_corpus)
    return returned_list
        
    
    
    