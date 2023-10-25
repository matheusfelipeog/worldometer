import re

from typing import Optional


def make_url(base_url: str, path_url: Optional[str] = None) -> str:
    url = base_url
    if path_url and re.match(r'^/{1}.*', path_url):
        url += path_url
    return url
