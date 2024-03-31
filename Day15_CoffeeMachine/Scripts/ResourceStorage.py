
class ResourceStorage:
    def __init__(self, water=0, coffee=0, milk=0, price=0.0):
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.price = price

    def print_data(self):
        print(f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: £{self.price}")

    def does_contain_enough(self, recipe_storage):
        if self.water < recipe_storage.water:
            print(f"The machine doesnt have enough water! (Stored: {self.water}) (Required: {recipe_storage.water})")
            return False
        if self.coffee < recipe_storage.coffee:
            print(f"The machine doesnt have enough coffee! (Stored: {self.coffee}) (Required: {recipe_storage.coffee})")
            return False
        if self.milk < recipe_storage.milk:
            print(f"The machine doesnt have enough milk! (Stored: {self.milk}) (Required: {recipe_storage.milk})")
            return False
        return True

    def make_purchase(self, recipe_storage):
        self.water -= recipe_storage.water
        self.coffee -= recipe_storage.coffee
        self.milk -= recipe_storage.milk
        self.price += recipe_storage.price