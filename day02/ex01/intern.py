class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name

    def __str__(self):
        return self.name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def make_coffee(self):
        return self.Coffee()

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")


def main():
    mark = Intern("Mark")
    anonymous = Intern()
    print(mark)
    print(anonymous)
    cup = mark.make_coffee()
    print(cup)
    try:
        anonymous.work()
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
