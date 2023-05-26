import mdforest

text = open("text4.md", "r").read()

cleaned = mdforest.clean_markdown(text)

with open("cleaned.md", "w") as f:
    f.write(cleaned)
