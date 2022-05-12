def print_numbers():
    with open("numbers.txt", "r") as file:
        for line in file.readlines():
            lineSplit = line.split(",")
            for number in lineSplit:
                print(number.strip("/n"))


if __name__ == '__main__':
    print_numbers()
