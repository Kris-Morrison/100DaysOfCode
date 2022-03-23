nativevlan = int(input ("What is your native vlan ? "))
datavlan = int(input ("What is your data vlan ? "))

if nativevlan == datavlan :
    print ("Change your data vlan !")
    if nativevlan == 1:
        print ("Your native vlan is default 1")
else:
    print ("Proceeed with your configuration")
