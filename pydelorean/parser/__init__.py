"""
    Copyright 2023 Keane Moraes

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

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