import settings
import sys


def create_result_file(filename: str):
    with open(filename, "r") as file:
        input_data = file.read()
        output_data = input_data.format(title=settings.title, name=settings.name,
                                        surname=settings.surname, age=settings.age, pro=settings.pro,
                                        skill1=settings.skill1, skill2=settings.skill2)
        with open("file.html", "w") as output_file:
            output_file.write(output_data)
        file.close()
        output_file.close()


def try_open_file(filename: str):
    try:
        open(filename, "r")
        return 1
    except IOError as error:
        print(error)
        sys.exit()


def main():
    if len(sys.argv) != 2:
        print("Bad argument")
        sys.exit()
    filename = sys.argv[1]
    if not filename.endswith(".template"):
        print("Bad argument")
        sys.exit()
    if try_open_file(filename):
        create_result_file(filename)


if __name__ == '__main__':
    main()
