class HotBeverage:
    def __init__(self):
        self.name = "hot beverage"
        self.price = 0.30

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        return f"name: {self.name}\n" \
               f"price: {self.price}\n" \
               f"description: {self.description()}"


class Coffee(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "coffee"
        self.price = 0.40

    def description(self):
        return "A coffee, to stay awake."



v = HotBeverage()
c = Coffee()
print(v)
print(c)

