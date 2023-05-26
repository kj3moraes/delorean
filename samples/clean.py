import mdforest

text = """

# Title

## Heading 1

## Heading 2

Hello [
    world
](https://www.google.com)!

This is **Bold text** and this is _italics_ why. 

This is an image: ![alt text](aslkdjflaksdjf.png) is where it is.

Hey there  <mark class="hltr-light-green">Some are held by the explicit profession of certain articles of faith</mark> allow it

"""

print(mdforest.clean_markdown(text))