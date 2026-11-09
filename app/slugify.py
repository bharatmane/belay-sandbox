import re


def slugify(text):
    return "-".join(re.findall(r"[a-z]+", text.lower()))
