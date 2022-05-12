import sys


def capital(argv):
    if len(argv) != 2:
        return 1
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }


if __name__ == '__main__':
    capital(sys.argv)
