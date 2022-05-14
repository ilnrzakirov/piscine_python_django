import beverages
import random


class CoffeeMachine:
    def __init__(self):
        self.count = 0

    class EmptyCup(beverages.HotBeverage):
        def __init__(self):
            super().__init__()
            self.price = 0.90
            self.name = "empty cup"

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            msg = "This coffee machine has to be repaired."
            super().__init__(self, msg)

    def repair(self):
        self.count = 0
        print("Machine repaired")

    def serve(self, beverage):
        if self.count > 9:
            raise self.BrokenMachineException
        self.count += 1
        rand = random.randint(0, 1)
        if rand == 1:
            return self.EmptyCup()
        return beverage()


def main():
    coffee = CoffeeMachine()
    for i in range(0, 10):
        try:
            print(coffee.serve(beverages.Coffee))
            print(coffee.serve(beverages.Tea))
            print(coffee.serve(beverages.Cappuccino))
            print(coffee.serve(beverages.Chocolate))
        except CoffeeMachine.BrokenMachineException as error:
            print(error)
            coffee.repair()


if __name__ == "__main__":
    main()
