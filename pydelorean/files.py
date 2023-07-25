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