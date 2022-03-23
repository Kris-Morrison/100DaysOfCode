from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

command = input("What drink would you like to choose: 'latte' 'espresso' 'cappuccino' \n")
#TODO 1. PRINT REPORT
if command == "report":
    print(CoffeeMaker.report())

#TODO 2 CHECK RESOURCE SUFFICIENT
resources = Menu.find_drink(command)
print(resources)

#TODO 3 PROCESS COINS

#TODO 4 CHECK TRANSACTION SUCCESSFUL

#TODO 5 MAKE COFFEE
CoffeeMaker.make_coffee()
