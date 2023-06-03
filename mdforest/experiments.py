import mdast

def process_node(node, parent_tree):
    if isinstance(node, mdast.Heading):
        header_level = node.depth
        header_text = node.children[0].value.strip()
        tree.create_node(f'{header_text}', f'{header_level}', parent=parent_tree)
        parent_tree = f'{header_level}'

    elif isinstance(node, mdast.Paragraph):
        paragraph_text = node.children[0].value.strip()
        tree.create_node(f'{paragraph_text}', f'{parent_tree}_p', parent=parent_tree)

    return parent_tree

markdown = '''
# Header 1
This is my first para
## Header 2
This is my second para
# Next Header 1
Hello friends
'''

ast = mdast.parse(markdown)
tree_list = []

parent_tree = None
current_tree = None

for node in ast.children:
    if isinstance(node, mdast.Heading):
        if current_tree:
            tree_list.append(current_tree)

        parent_tree = None
        current_tree = mdast.Tree(node)

    parent_tree = process_node(node, parent_tree)

if current_tree:
    tree_list.append(current_tree)

for tree in tree_list:
    tree.show()
