import sys


def main():
    if len(sys.argv) != 2:
        print("Bad argument")
        sys.exit()
    filename = sys.argv[1]
    if not filename.endswith(".template"):
        print("Bad argument")
        sys.exit()


if __name__ == '__main__':
    main()