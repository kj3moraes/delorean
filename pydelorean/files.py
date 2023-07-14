

class File:
    pass

# FIGUREOUT: Do we really need a file class for each of the supported formats ?
# FIGUREOUT: What more attributes / methods should these classes have ?

class MarkdownFile(File):
    pass

class RestructuredFile(File):
    pass

class AsciidocFile(File):
    pass

class TextFile(File):
    pass

class YAMLFile(File):
    pass

class JSONFile(File):
    pass


FILE_EXTENSIONS = {
    ".md":      MarkdownFile,
    ".rst":     RestructuredFile,
    ".adoc":    AsciidocFile,
    ".txt":     TextFile,
    ".yaml":    YAMLFile,
    ".yml":     YAMLFile,
    ".json":    JSONFile
}