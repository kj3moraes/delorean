from .parser import *


PARSER_CLASSES = {
    ".md"  : MarkdownParser,
    ".rst" : RestructuredParser,
    ".adoc": AsciiDocParser,
    ".yaml": YAMLParser,
    ".yml" : YAMLParser,
    ".json": JSONParser,
    ".xml" : XMLParser
}

def get_parser_from_extension(extension:str) -> Parser:
    """
    Returns the parser class that corresponds to the given extension.
    """
    return PARSER_CLASSES[extension]


def get_parser_from_document_name(document_name:str) -> Parser:
    """
    Returns the parser class that corresponds to the given document name.
    """
    file_extension = document_name.split('.')[-1]
    return get_parser_from_extension(file_extension)