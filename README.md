# Markdown Tree

markdown-tree is a fork of [md2py](https://github.com/alvinwan/md2py) which is no longer maintained. This library adds far more functionality and broadens the scope of the older libary. The full list of features can be found under [Features](## Features)

## Install 

Install via pip
```bash
pip install markdown-tree
```

You can find the library [here](nil)

## Quick Usage Guide 

Markdown2Python offers only one function `md2py`, which generates a Python
object from markdown text. This object is a navigable, "Tree of Contents"
abstraction for the markdown file.

Take, for example, the following markdown file.

**chikin.md**

```
# Chikin Tales

## Chapter 1 : Chikin Fly

Chickens don't fly. They do only the following:

- waddle
- plop

### Waddling

## Chapter 2 : Chikin Scream

### Plopping

Plopping involves three steps:

1. squawk
2. plop
3. repeat, unless ordered to squat

### I Scream
```

Akin to a navigation bar, the `TreeOfContents` object allows you to expand a
markdown file one level at a time. Running `md2py` on the above markdown file
will generate a tree, abstracting the below structure.

```
          Chikin Tales
          /           \
    Chapter 1       Chapter 2
      /               /     \
  Waddling      Plopping    I Scream
```

For the full usage guide, access the SAMPLES.md file.

## Features 

Some of the features of this library are:
1. Converts a markdown file to a manipulatable, light Python data structure 
2. Converts the Python data structure back into a Markdown file.
3. Traverse and edit the Python data structure. 

## License 
The [original project](https://github.com/alvinwan/md2py) was licensed under the Apache 2.0 License and a copy is provided in this repo as well. All the files changed are listed in the CHANGELOG. 
