
import data
import sandwich_maker
import cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()



def main():
    ###  write the rest of the codes ###
    turned_on = True
    while turned_on:
        select = input("What would you like? (small/ medium/ large/ off/ report)")
        if select == "off":
            turned_on = False
        elif select == 'report':
            for item, amount in sandwich_maker_instance.machine_resources.items():
                print(f"{item} : {amount}")

        elif select in recipes:
            sandwich = recipes[select]

            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                coins = cashier_instance.process_coins()

                if cashier_instance.transaction_result(coins, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(select, sandwich["ingredients"])
        else:
            print("Couldn't create sandwich.")

if __name__=="__main__":
    main()
