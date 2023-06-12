.. image:: media/image.png
   :width: 200

delorean
==========================

A library to convert markup documents into tree data structures and
vice versa. There is greater functionality available to modify, prune,
add and delete parts of documents when there are in the MarkdownTree
structure.

The full list of features can be found under `Features <##%20Features>`__

Install
-------

Install via pip

.. code:: bash

   pip install pydelorean

You can find the library page here `here <nil>`__

Quick Usage Guide
-----------------

delorean offers only one function ``treeify``, which generates a
Python object from markup text. The object is a [treelib](https://github.com/caesar0301/treelib) Tree structure.

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

This project is licensed under the Apache 2.0 License. A copy of the license 
can be found in the LICENSE file.