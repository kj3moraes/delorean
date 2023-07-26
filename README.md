<img style="float: left; padding:20px" src="media/image.png" alt="pydelorean" width="150"/>

# delorean

A library to convert markup documents into tree data structures and vice versa. There is greater functionality available to modify, prune, add and delete parts of documents when there are in the MarkdownTree
structure.

The full list of features can be found in FEATURES.md or in the documentation.

## Install

Install via pip

```bash
pip install pydelorean
```

You can find the library page here [here](https://pypi.org/project/pydelorean/)

## Quick Usage Guide

The library can be used to convert markdown documents into forest data strucutre. Using just the treeify command on the following text

```markdown
chikin.md

# Chikin Tales
Once there was a chikin.
## Chapter 1 : Chikin Fly
Chickens don't fly. They do only the following:
- waddle
- plop 
### Waddling
A waddle is what these birds do.
## Chapter 2 : Chikin Scream
### Plopping
Plopping involves three steps:
1. squawk
2. plop
3. repeat, unless ordered to squat
```

```python
from pydelorean import treeify
tree = treeify(text)
print(tree)
```

```txt
                   Chikin Tales
                  /     \       \
                 /       \       \
           (Once th..)    |       \
                          |        \
                      Chapter 1     \
                      /     |     Chapter 2
                     /      |         |
           (Chickens do..)  |       Plopping
                            |         |
                         Waddling   (Plopping...)
                            |
                        (A waddle...)

```

```python
shift_nodes(tree, ["chikin.md/# Chikin Tales/## Chapter 2 : Chikin Scream"], ["chikin.md/# Chikin Tales/## Chapter 1/## Chapter 2"])
```

```txt
                   Chikin Tales
                  /     \       
                 /       \       
           (Once th..)    |       
                          |        
                      Chapter 1----\
                       |    |       \
                      /     |     Chapter 2
                     /      |         |
           (Chickens do..)  |       Plopping
                            |         |
                         Waddling   (Plopping...)
                            |
                        (A waddle...)

```

For a quick usage guide, see the `samples/` directory for some examples.

For a detailed description, check the documentation page here - [pydelorean docs](https://readthedocs.org/projects/pydelorean/)

## Features

Some of the features of this library are:

- forest data structure for Markdown, reStructuredText, AsciiDoc, JSON, YAML and XML.
- 'cleaning' of documents to remove unwanted elements.
- document manipulation using the tree data structure.
- document generation from tree data structure.

## License

This project is licensed under the Apache 2.0 License. A copy of the license can be found in the LICENSE file.
