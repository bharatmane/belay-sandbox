import re


def slugify(text):
    """Convert text to a lowercase, hyphen-separated slug.

    The text is lowercased, then every run of ASCII letters (a-z) is kept
    and the runs are joined with single hyphens. Any other character,
    including spaces and punctuation, only separates words and is dropped.

    Example: slugify("Hello, World!") returns "hello-world".
    """
    return "-".join(re.findall(r"[a-z]+", text.lower()))
