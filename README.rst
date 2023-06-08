.. image:: media/forest-icon.png
   :width: 100

mdforest - Markdown Forest
==========================

A library to convert Markdown documents into tree data structures and
vice versa. There is greater functionality available to modify, prune,
add and delete parts of documents when there are in the MarkdownTree
structure.

markdown-tree is a fork of `md2py <https://github.com/alvinwan/md2py>`__
which is no longer maintained. This library adds far more functionality
and broadens the scope of the older libary. The full list of features
can be found under `Features <##%20Features>`__

Install
-------

Install via pip

.. code:: bash

   pip install markdown-tree

You can find the library page here `here <nil>`__

Quick Usage Guide
-----------------

Markdown2Python offers only one function ``md2py``, which generates a
Python object from markdown text. This object is a navigable, “Tree of
Contents” abstraction for the markdown file.

Take, for example, the following markdown file.

[[ chikin.md ]]

.. code:: markdown

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

Akin to a navigation bar, the ``TreeOfContents`` object allows you to
expand a markdown file one level at a time. Running ``md2py`` on the
above markdown file will generate a tree, abstracting the below
structure.

.. code:: text

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

For the full usage guide, access the SAMPLES.md file.

Features
--------

Some of the features of this library are:

1. Converts a markdown file to a manipulatable, light Python data
   structure.
2. Converts the Python data structure back into a Markdown file.
3. Traverse and edit the Python data structure.

License
-------

The `original project <https://github.com/alvinwan/md2py>`__ was
licensed under the Apache 2.0 License and a copy is provided in this
repo as well. All the files changed are listed in the CHANGELOG.
