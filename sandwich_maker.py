class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for food, amount in order_ingredients.items():
            self.machine_resources[food] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")