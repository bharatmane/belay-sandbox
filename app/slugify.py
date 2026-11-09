import re


def slugify(text):
    return "-".join(re.findall(r"[a-z0-9]+", text.lower()))
