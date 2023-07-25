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

from bs4 import BeautifulSoup
from .delorean import *
from .base import Forest
import re


# TODO: Check the type of the input and call the appropriate function
# Use the newly defined File classes for this. 
def treeify(name:str, text:str, *args, **kwargs) -> Forest:
    
    return mdtreeify(name, text, *args, **kwargs)


def textify(forest:Forest, *args, **kwargs) -> str:
    
    return mdtextify(forest)

