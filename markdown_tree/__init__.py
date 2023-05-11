from .md2py import TreeOfContents


def markdown_tree(md, *args, **kwargs):
    """
    Converts markdown file Python object

    :param str md: markdown string
    :return: object
    """
    return TreeOfContents.fromMarkdown(md, *args, **kwargs)
