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
    input_value = argv[1]
    key_for_capital_cities = ""
    for key, value in states.items():
        if key == input_value:
            key_for_capital_cities = value
            break
    for key, value in capital_cities.items():
        if key_for_capital_cities == key:
            print(value)
            return 0
    print("Unknown state")


if __name__ == '__main__':
    capital(sys.argv)
