from markdown import markdown
from bs4 import BeautifulSoup
import re

class __TreeOfContents:
    """Tree abstraction for markdown source"""

    source_type = BeautifulSoup
    valid_tags = ('a', 'abbr', 'address', 'area', 'article', 'aside', 'audio',
        'b', 'base', 'bdi', 'bdo', 'blockquote', 'body', 'br', 'button',
        'canvas', 'caption', 'cite', 'code', 'col', 'colgroup', 'data',
        'datalist', 'dd', 'del', 'details', 'dfn', 'dialog', 'div', 'dl', 'dt',
        'em', 'embed', 'fieldset', 'figcaption', 'figure', 'footer', 'form',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hgroup', 'hr',
        'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'keygen', 'label',
        'legend', 'li', 'link', 'main', 'map', 'mark', 'menu', 'menuitem',
        'meta', 'meter', 'nav', 'noscript', 'object', 'ol', 'optgroup',
        'option', 'output', 'p', 'param', 'picture', 'pre', 'progress', 'q',
        'rp', 'rt', 'ruby', 's', 'samp', 'script', 'section', 'select', 'small',
        'source', 'span', 'strong', 'style', 'sub', 'summary', 'sup', 'table',
        'tbody', 'td', 'template', 'textarea', 'tfoot', 'th', 'thead', 'time',
        'title', 'tr', 'track', 'u', 'ul', 'var', 'video', 'wbr')
    allowed_attrs = ('string', 'name')

    def __init__(self, root, branches=(), descendants=(), source=None,
        depth=None):
        """
        Construct TreeOfContents object using source

        :param SourceType source: parsed source
        :param list TreeOfContents branches: list of direct children
        :param list SourceType descendants: all descendants
        """
        assert source is not None, 'NoneType source passed into TreeOfContents'
        self.source = source
        self.depth = depth or self.parseTopDepth()
        self.descendants = descendants or self.expandDescendants(branches)
        self.branches = branches or self.parseBranches(descendants)

    @staticmethod
    def getHeadingLevel(bs):
        """
        Return heading level of BeautifulSoup object
        """
        try:
            return int(bs.name[1])
        except (ValueError, IndexError, TypeError):
            return None

    def parseTopDepth(self):
        """
        Parse highest heading in markdown
        """
        for i in range(1, 7):
            if getattr(self.source, 'h%d' % i):
                return i

    def expandDescendants(self, branches):
        """
        Expand descendants from list of branches

        :param list branches: list of immediate children as TreeOfContents objs
        :return: list of all descendants
        """
        return sum([b.descendants() for b in branches], []) + [b.source for b in branches]

    def parseBranches(self, descendants):
        """
        Parse top level of markdown

        :param list elements: list of source objects
        :return: list of filtered TreeOfContents objects
        """
        parsed, parent, cond = [], False, lambda b: (b.string or '').strip()
        for branch in filter(cond, descendants):
            if self.getHeadingLevel(branch) == self.depth:
                parsed.append({'root':branch.string, 'source':branch})
                parent = True
            elif not parent:
                parsed.append({'root':branch.string, 'source':branch})
            else:
                parsed[-1].setdefault('descendants', []).append(branch)
        if self.depth == None:
            return [TOC(depth=1, **kwargs) for kwargs in parsed]
        return [TOC(depth=self.depth+1, **kwargs) for kwargs in parsed]

    def __getattr__(self, attr, *default):
        """Check source for attributes"""
        tag = attr[:-1]
        if attr in self.allowed_attrs:
            return getattr(self.source, attr, *default)
        if attr in self.valid_tags:
            return next(filter(lambda t: t.name == attr, self.branches), None)
        if len(default):
            return default[0]
        if attr[-1] == 's' and tag in self.valid_tags:
            condition = lambda t: t.name == tag
            return filter(condition, self.branches)
        raise AttributeError("'TreeOfContents' object has no attribute '%s'" % attr)

    def __repr__(self):
        """Display contents"""
        return str(self)

    def __str__(self):
        """Display contents"""
        return self.string or ''

    def __iter__(self):
        """Iterator over children"""
        return iter(self.branches)

    def __getitem__(self, i):
        return self.branches[i]

    @staticmethod
    def fromMarkdown(md, *args, **kwargs):
        """
        Creates abstraction using path to file
        """
                
        def clean_headers(markdown_text):
            """ 
            Remove bold and italics formatting from headers
            """
            
            # Regular expressions to match bold and italics formatting
            bold_pattern = re.compile(r'\*\*(.*?)\*\*')
            alt_bold_pattern = re.compile(r'__(.*?)__')
            italics_pattern = re.compile(r'\*(.*?)\*')
            alt_italics_pattern = re.compile(r'_(.*?)_')

            # Split the Markdown text into lines
            lines = markdown_text.splitlines()

            # Iterate through the lines
            for i in range(len(lines)):
                line = lines[i]

                # Check if the line starts with one or more hash characters (header)
                if line.startswith('#'):
                    # Remove bold formatting
                    line = bold_pattern.sub(r'\1', line)
                    line = alt_bold_pattern.sub(r'\1', line)

                    # Remove italics formatting
                    line = italics_pattern.sub(r'\1', line)
                    line = alt_italics_pattern.sub(r'\1', line)

                    # Update the line in the list of lines
                    lines[i] = line

            # Join the modified lines back into a single string
            modified_text = '\n'.join(lines)
            return modified_text
    
        md = clean_headers(md)
        html_convert = markdown(md, *args, **kwargs)
        source = BeautifulSoup(html_convert, 'html.parser', *args, **kwargs)
        return TOC('[document]',
                    source=source,
                    descendants=source.children)

TOC = __TreeOfContents
