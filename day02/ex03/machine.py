import beverages
import random


class CoffeeMachine:
    def __init__(self):
        self.count = 0

    class EmptyCup(beverages.HotBeverage):
        price = 0.90
        name = "empty cup"

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            msg = "This coffee machine has to be repaired."
            super().__init__(self, msg)

    def repair(self):
        self.count = 0
        print("Machine repaired")

