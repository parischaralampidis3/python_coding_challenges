import re

def introduction():
    print ("Welcome at the madlibs game!\n")
    print("Please fill the gaps with the right choise.\n")
    print("Are you ready to continue?\n")
    print("Type y/Y for yes, or n/N for no, to continue..")
introduction()

def input_choice():
    decision = input("> ")
    print(decision)
    if decision == 'Yes' or decision == 'yes':
         print("It was yes")
    elif decision == 'No' or decision == 'no':
        print("no")
    else:
        print("sorry i dont understand")

   

input_choice()
   


   
       



