Salary = float(input("What is your salary : £"))
print("-------------")
if Salary >= 1000:

    if Salary >= 2000:
        Tax = Salary*20/100
        print ("Taxed 20%")
    else:
        Tax = Salary*15/100
        print ("Taxed 15%")

else:

    Tax = 0
    print("No Tax deducted")

Net = Salary - Tax

print("-------------")
print("Tax : £", Tax)
print("Net Pay : £", round(Net))
