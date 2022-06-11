from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

make_coffee = True
my_coffee = CoffeeMaker()
my_menu = Menu()
my_payment = MoneyMachine()
while make_coffee:
    coffee = input("What would you like? (espresso/latte/cappuccino/):")
    if coffee == "report":
        my_coffee.report()
    else:
        drink = my_menu.find_drink(coffee)
        drink_status = my_coffee.is_resource_sufficient(drink) and my_payment.make_payment(drink.cost)
        if drink_status:
            my_coffee.make_coffee(drink)
          
        else:
            print(drink_status)
            print(my_payment.report())
            make_coffee = False