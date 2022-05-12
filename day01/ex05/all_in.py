import sys

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


def find_state(input_value):
    key_for_capital_cities = ""
    for key, value in capital_cities.items():
        if value == input_value:
            key_for_capital_cities = key
            break
    for key, value in states.items():
        if key_for_capital_cities == value:
            return key


def find_capital(input_value):
    key_for_capital_cities = ""
    for key, value in states.items():
        if key == input_value:
            key_for_capital_cities = value
            break
    for key, value in capital_cities.items():
        if key_for_capital_cities == key:
            return value


def find_dict(word: str):
    state = find_state(word)
    capital = find_capital(word)


def find(argv):
    if len(argv) != 2:
        return 1
    input_date = argv[1].split(",")
    for input_word in input_date:
        word = input_word.strip(" ")
        if len(word) > 0:
            find_dict(word)


if __name__ == '__main__':
    find(sys.argv)
