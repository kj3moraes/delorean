import pydelorean

text = open("text4.md", "r").read()

cleaned = pydelorean.clean_markdown(text)

with open("cleaned.md", "w") as f:
    f.write(cleaned)
