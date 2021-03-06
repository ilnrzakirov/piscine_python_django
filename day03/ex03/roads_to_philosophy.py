import sys
import requests
from bs4 import BeautifulSoup


def search_phil(word, titleList):
    global response
    if word.startswith("/wiki/"):
        word = word.replace("/wiki/", "")
    url = f'https://en.wikipedia.org/wiki/{word}'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as error:
        if response.status_code == 404:
            print("page not found")
            return
        print(error)
        return
    data = BeautifulSoup(response.text, 'html.parser')
    title = data.find(id='firstHeading').text
    if title in titleList:
        print("Loop")
        return
    titleList.append(title)
    print(title)
    if title == "Philosophy":
        print(f"{len(titleList)} roads from to Philosophy")
        sys.exit()
    content = data.find(id="mw-content-text")
    links = content.select("p > a")
    for link in links:
        if link.get('href') is not None and link['href'].startswith('/wiki/') \
                and not link['href'].startswith('/wiki/Wikipedia:') and not link['href'].startswith('/wiki/Help:') and \
                '.' not in link['href'] and ':' not in link['href'] and not link['href'].startswith("/wiki/File:"):
            return search_phil(link["href"], titleList)
    print("It's a dead end !")
    return


def main():
    titleList = []
    if len(sys.argv) != 2:
        print("Bad argument")
        sys.exit()
    if len(sys.argv) == 2:
        search_phil(sys.argv[1], titleList)


if __name__ == '__main__':
    main()
