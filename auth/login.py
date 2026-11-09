import re

USERNAME_RE = re.compile(r"^[A-Za-z0-9_.-]+$")


def valid_username(name):
    return bool(USERNAME_RE.match(name))
