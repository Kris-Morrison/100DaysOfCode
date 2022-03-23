from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
while is_on:
    drinks = menu.get_items()
    command = input(f"What drink would you like to choose: {drinks} \n")

    #TODO 1. PRINT REPORT
    if command == "stop":
        is_on = False
    if command == "report":
        coffeemaker.report()
        money_machine.report()

    if command == "latte" or command == "espresso" or command == "cappuccino":
        drink = Menu().find_drink(command)


    #TODO 2 CHECK RESOURCE SUFFICIENT
        Resource_check = CoffeeMaker().is_resource_sufficient(drink)

    #TODO 3 PROCESS COINS
        Money = MoneyMachine().make_payment(drink.cost)

    #TODO 4 CHECK TRANSACTION SUCCESSFUL
        if Resource_check == True and Money == True:
            #TODO 5 MAKE COFFEE
            coffeemaker.make_coffee(drink)

