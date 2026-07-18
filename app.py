import re


def slugify_title(title: str) -> str:
    """Convert a title into a URL-safe slug.

    Returns a lowercased string containing only ASCII letters, digits, and
    internal hyphens.  Each maximal sequence of non-alphanumeric characters
    collapses to a single hyphen.  Leading and trailing hyphens are removed.
    Empty input or input containing no ASCII letters or digits returns the
    empty string.
    """
    if not isinstance(title, str):
        raise TypeError("title must be a string")

    stripped = title.strip()

    slug = re.sub(r"[^A-Za-z0-9]+", "-", stripped)

    slug = slug.lower()

    slug = slug.strip("-")

    return slug


def validate_title(title: str) -> str:
    if not isinstance(title, str):
        raise TypeError("title must be a string")

    trimmed = title.strip()

    if not trimmed:
        raise ValueError("title must not be empty")

    if len(trimmed) > 80:
        raise ValueError("title must not exceed 80 characters")

    return trimmed
