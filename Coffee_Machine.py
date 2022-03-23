import Coffee_Shop
from replit import clear


def stock_check(coffee, stock, menu):
    check = ["Water", "Milk", "Coffee"]
    for component in check:
        stock_enough = "yes"
        if stock_enough == "yes":
            requirements = menu[coffee]["ingredients"][component]
            component_stock = stock[component]
            if requirements > component_stock:
                stock_enough = "no"
                return stock_enough
            else:
                stock_enough = "yes"
    return stock_enough


def stock_remove(coffee, stock, menu):
    check = ["Water", "Milk", "Coffee"]
    for component in check:
        requirements = menu[coffee]["ingredients"][component]
        stock[component] -= requirements


current_resources = Coffee_Shop.resources
system_on = "on"
Menu = Coffee_Shop.MENU
while system_on == "on":

    # TODO 1.What coffee would you like to choose
    command = str(input("What is your choice of drink: (espresso/latte/cappuccino) \n")).lower()
    clear()

    # TODO 1.1 Carry out additional tasks not detailed
    # Switches the coffee machine and resets all stock counters
    if command == "stop":
        system_on = "off"
    else:
        system_on = "on"

    if command == "restock":
        current_resources["Water"] = 300
        current_resources["Milk"] = 200
        current_resources["Coffee"] = 100

    if command == "report":
        for resource in current_resources:
            print(f'{resource} : {current_resources[resource]}')

    # TODO 2.Check coffee requirements against coffee machine resources
    if command == "espresso" or command == "latte" or command == "cappuccino":
        enough_stock = stock_check(command, current_resources, Menu)

        if enough_stock == "yes":

            # TODO 3.what coins have been entered into the machine
            cost_of_coffee = Coffee_Shop.MENU[command]["cost"]
            print(f"cost of the coffee: £{cost_of_coffee}")
            pound_coins = int(input("How many £1 coins have you entered?: \n"))
            fifty_coins = int(input("How many £0.50 coins have you entered?: \n"))
            twenty_coins = int(input("How many £0.20 coins have you entered?: \n"))
            ten_coins = int(input("How many £0.10 coins have you entered?: \n"))
            clear()
            total_paid = float((pound_coins * 1) + (fifty_coins * 0.5) + (twenty_coins * 0.2) + (ten_coins * 0.1))

            if total_paid < cost_of_coffee:
                print(f"Your have not paid the value of the coffee, £{cost_of_coffee} \n Here is your refund. ")

            elif total_paid >= cost_of_coffee:
                # TODO 4. if paid for, make coffee and remove stock etc
                change = total_paid - cost_of_coffee
                Coffee_Shop.resources["Money"] += cost_of_coffee
                stock_remove(command, current_resources, Menu)
                print(f"Enjoy your coffee and have a good day! here is your change £{change}")

        elif enough_stock == "no":
            print("""we are unable to provide you your drink, due to shortage of stock inside the machine. \n Please inform a member of staff""")




