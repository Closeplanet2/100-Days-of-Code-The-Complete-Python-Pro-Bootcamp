from Scripts.ResourceStorage import ResourceStorage
from Scripts.PlayerInput import string_input, float_input

class CoffeeMachine:
    def __init__(self, water=0, coffee=0, milk=0, price=0, loop_once=False):
        self.loop_once = loop_once
        self.stored_liquid = ResourceStorage(water, coffee, milk, price)
        self.stored_recipes = {}

    def add_stored_recipe(self, recipe_name, water, coffee, milk, price):
        self.stored_recipes[recipe_name] = ResourceStorage(water, coffee, milk, price)

    def return_names_of_stored_recipes(self):
        return "/".join(self.stored_recipes.keys())

    def return_names_of_stored_recipes_as_array(self, other_values=None):
        if other_values is None:
            other_values = []
        return list(self.stored_recipes.keys()) + other_values

    def game_loop(self):
        if not self.stored_recipes:
            return
        while True:
            stored_names = self.return_names_of_stored_recipes()
            accepted_answers = self.return_names_of_stored_recipes_as_array(["Report", "Off"])
            user_input = string_input(f"Would you like? ({stored_names}): ", correct_values=accepted_answers)

            if user_input == "Off":
                print("Machine is turning off!")
                return

            if user_input == "Report":
                self.stored_liquid.print_data()
                continue

            stored_recipe = self.stored_recipes.get(user_input)
            if not stored_recipe:
                print("Invalid choice! Please select a valid option.")
                continue

            if not self.stored_liquid.does_contain_enough(stored_recipe):
                continue

            total_user_money = float_input(f"How much are you paying with? (Total Price: £{stored_recipe.price}) £")
            while total_user_money < stored_recipe.price:
                print(f"You haven't added enough money into the system! Amount to pay: £{stored_recipe.price - total_user_money}")
                total_user_money += float_input(f"How much extra are you paying? £")

            if total_user_money > stored_recipe.price:
                total_user_change = total_user_money - stored_recipe.price
                print(f"Here is your £{total_user_change} in change")

            print(f"Here is your {user_input}! Enjoy your day")
            self.stored_liquid.make_purchase(stored_recipe)

            if self.loop_once:
                return
            else:
                print("\n\n\n\n\n")
