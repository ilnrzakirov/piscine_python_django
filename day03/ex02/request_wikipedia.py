import sys
import requests
import dewiki


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

    response = request.get(url=url, params=params)
    data = response.json()
    try:
        output_data = dewiki.from_string(data['parse']['wikitext'])
        with open(f"{sys.argv[1]}.wiki", "w") as file:
            file.write(output_data.replace("\n\n", "\n"))
    except KeyError as error:
        print("Try again")


if __name__ == '__main__':
    main()