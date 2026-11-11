import re

MAX_LENGTH = 50


def slugify(text):
    slug = "-".join(re.findall(r"[a-z]+", text.lower()))
    return slug[:MAX_LENGTH].rstrip("-")
