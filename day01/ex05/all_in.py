import sys


def find_state(input_value):
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
    key_for_capital_cities = ""
    for key, value in capital_cities.items():
        if value.lower() == input_value.strip().title().lower():
            key_for_capital_cities = key.lower()
            break
    for key, value in states.items():
        if key_for_capital_cities == value.lower():
            return key
    return None


def find_capital(input_value):
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
    key_for_capital_cities = ""
    for key, value in states.items():
        if key.lower() == input_value.strip().title().lower():
            key_for_capital_cities = value.lower()
            break
    for key, value in capital_cities.items():
        if key_for_capital_cities == key.lower().lower():
            return value
    return None


def find_word(word: str):
    wordList = ["Oregon", "Alabama", "New Jersey", "Colorado", "Salem", "Montgomery", "Trenton", "Denver"]
    for elem in wordList:
        if elem.lower() == word.lower().strip():
            return elem


def find_dict(word: str):
    state = find_state(word.lower())
    capital = find_capital(word.lower())
    res_word = find_word(word)
    if state:
        print(f"{res_word} is the capital of {state}")
    elif capital:
        print(f"{capital} is the capital of {res_word}")
    else:
        print(f"{word} is neither a capital city nor a state")


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
