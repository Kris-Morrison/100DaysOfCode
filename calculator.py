from html.entities import name2codepoint
from tkinter import N

def calculator():
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2 

    def divide(n1, n2):
        return n1 / n2


    operations = {"+": add, "-": subtract, "*":multiply, "/":divide}

    n1 = float(input("Whats your first number? "))
    n2 = float(input("Whats your second number? "))
    for operation in operations:
        print(operation)
    operater = input("What operator would you like to use? ")
    function = operations[operater]
    answer1 = function(n1,n2)

    print(f"{n1} {operater} {n2} = {answer1}")

    con = input("Would you like to continue on you calculator? 'yes' or 'no'. \nIf you like to start a new calculation, type 'r'' : ")
    while con == "yes":

        operater2 = input("What operator would you like to use? ")
        n3 = float(input("Whats your third number? "))
        function = operations[operater2]
        answer2 = function(answer1,n3)
        
        print(f"{answer1} {operater2} {n3} = {answer2}")
        answer1 = answer2
        con = input("Would you like to continue on you calculator? 'yes' or 'no'.\nIf you like to start a new calculation, type 'r'' : ")
    if con == "r":
        calculator()
    
calculator()