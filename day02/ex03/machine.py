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
