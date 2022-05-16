import sys

import requests


def main():
    if len(sys.argv) != 2:
        print("bad argument")

    request = requests.Session()
    url = 'https://en.wikipedia.org/w/api.php'

    params = {
        "action": "parse",
        "page": sys.argv[1],
        "prop": "wikitext",
        "format": "json",
        "redirects": True,
        "formatversion": 2
    }
