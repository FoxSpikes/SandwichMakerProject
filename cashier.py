class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        ###
        total = 0
        print("input money here:")
        dollars = int(input("how many dollars? ")) * 1
        halfdollars = int(input("how many half dollars? ")) * .5
        quarters = int(input("how many quarters? ")) * .25
        nickels = int(input("how many nickels? ")) * .05
        total += dollars + halfdollars + quarters + nickels
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##
        if coins >= cost:
            giveback = coins - cost
            print(f"Here is ${giveback} in change")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False