from enum import Enum

# TODO; Rewrite this to be more generic and maybe have classes here instead of enums
class FileType(Enum):
    MARKDOWN            = "md"
    RESTRUCTUREDTEXT    = "rst"
    TEXT                = "txt"
    JSON                = "json"
    YAML                = "yaml"
    

class Error(Exception):
    pass