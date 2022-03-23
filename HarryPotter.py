print("""
      
            _            _.,----,
 __  _.-._ / '-.        -  ,._  \) 
|  `-)_   '-.   \       / < _ )/" }
/__    '-.   \   '-, ___(c-(6)=(6)
 , `'.    `._ '.  _,'   >\    "  )
 :;;,,'-._   '---' (  ( "/`. -='/
;:;;:;;,  '..__    ,`-.`)'- '--'
;';:;;;;;'-._ /'._|   Y/   _/' \
      '''"._ F    |  _/ _.'._   `\
             L    \   \/     '._  \
      .-,-,_ |     `.  `'---,  \_ _|
      //    'L    /  \,   ("--',=`)7
     | `._       : _,  \  /'`-._L,_'-._
     '--' '-.\__/ _L   .`'         './/
                 [ (  /
                  ) `{
                  \__)
""")
print("Welcome to Hogwarts.")
print("Your mission is to find the Chamber of Secrets.")

#Write your code below this line 👇
stage1 = input("""You have found a clue that tells you where in the school the enterence is to the chamber of secrets, do you continue?  \"Y\"or \"N\" \n""")

if stage1 == "Y":
    print("You have succesfully entered the chamber ")
    print("""
    o'')}____//
     `_/      )
    (_(_/-(_/
     """)
    stage2 = input("You have been encountered by a three headed dog, trying to attack you! Do you use your \"WAND\" or \"RUN\" away \n")
    if stage2 == "WAND":
         print("You have killed the dog and found a hatch under the dog. You continue your conquest ")
         stage3 = input("Your encountered by the Basilisk, do you stab it with the \"SWORD\" or attack with the \"WAND\" \n ")
         if stage3 == "SWORD":
                print("You have killed the Basilisk and you have completed the Chamber of Secrets! ")
         elif stage3 == "WAND":
                print("The wand has had no affect on the monster and you have to run! GAME OVER! " )
         else:
                print("Please enter either SWORD or WAND. GAME OVER! ")     
    elif stage2 == "RUN":
            print("The Chamber of secrets will never be found now. GAME OVER! ")
    else:
            print("Please enter either WAND or RUN. GAME OVER! ")
elif stage1 == "N":
    print("The Chamber of secrets will never be found now. GAME OVER! ")
else:
    print("Please enter either Y or N. GAME OVER! ")