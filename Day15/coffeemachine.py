MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coffee_choice():
    money_type = ["quarters", "dimes", "nickels", "pennies"]
    choice = input("What would you like? (espresso/latte/cappuccino):")

    #Check money
    def money():
        cost_total = 0
        if choice == "report":
            for k,v in resources.items():
                print(f"{k}: {v}")
            coffee_choice()
        
        if choice == "off":
            exit(0)

    
        for k,v in MENU.items():
            if choice == k:
                if choice == "espresso":
                    pass
                else:
                    if resources["milk"] >= MENU[k]["ingredients"]["milk"] :
                        resources["milk"] = resources["milk"] - MENU[k]["ingredients"]["milk"]
                    else:
                        print("There is not enough milk")
                        coffee_choice()

            if choice == k:
                if resources["coffee"] >= MENU[k]["ingredients"]["coffee"] :
                    resources["coffee"] = resources["coffee"] - MENU[k]["ingredients"]["coffee"]
                else:
                    print("Sorry there is not enough coffee")
                    coffee_choice()

            if choice == k:
                if resources["water"] >= MENU[k]["ingredients"]["water"] :
                    resources["water"] = resources["water"] - MENU[k]["ingredients"]["water"]
                else:
                    print("Sorry there is not enough water")
                    coffee_choice()

        def cost(quarters):
            price_input = int(input(f"how many {quarters}?"))
            if i == "quarters":
                final_price = price_input * 0.25
            elif i == "dimes":
                final_price = price_input * 0.10

            elif i =="nickels":
                final_price = price_input * 0.05
            
            elif i == "pennies":
                final_price = price_input * 0.01
            
            return final_price



        for i in money_type:
            cost_money = cost(i)
            cost_total = round(cost_money,2) + round(cost_total,2)
        print(cost_total)
        
        if cost_total < MENU[choice]["cost"]:
            print("................................................")
            print("Sorry that's not enough money. Money refunded.")
            print(".......................................")
            coffee_choice()
        else:
            print("Please insert coin")
            print("Coin Inserted")
            refund = cost_total - MENU[choice]["cost"]
            print("....................................")
            print(f"Here is your {choice}. Enjoy!")
            print(f"Here's your refund of {refund}$")
            print(".....................................")
            coffee_choice()

    money()

    

coffee_choice()