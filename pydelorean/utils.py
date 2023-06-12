from enum import Enum


class FileType(Enum):
    MARKDOWN            = "md"
    RESTRUCTUREDTEXT    = "rst"
    TEXT                = "txt"
    JSON                = "json"
    YAML                = "yaml"
    

class Error(Exception):
    pass