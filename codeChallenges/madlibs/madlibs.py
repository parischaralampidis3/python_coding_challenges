
#call introduction function for the game
def introduction():
    print ("Welcome at the madlibs game!\n")
    print("Please fill the gaps, while type the right number of the choise.\n")
introduction()
#add a function that you will be able to call inside the game.
def enter_stage():
     print("Your challenge comes.")
     print("type the number of the correct choice.") 
enter_stage()

#this is the main block function, of the question challenge for the gam
def first_stage(attr1,attr2,attr3):   
    print("Little lamp, sweet and fat, his mothers only _____\n")
    print("1 [proud]\n")
    print("2 [count \n")
    print("3 [pound]\n")

    first_stage = input ("> ")
    if first_stage == attr1:
        print ("Correct!")
    elif first_stage == attr2 or first_stage == attr3:
        print("not correct")
    else:
        print("sorry i don't understand")
first_stage("1","2","3")

#validate the choice of the user
def input_choice(attr1,attr2,attr3,attr4):    
    print("Are you ready to continue?\n")
    print("Type y/Y for yes, or n/N for no, to continue..")
    decision = input("> ")
    print(decision)
    if decision == attr1 or decision == attr2:
         print("Please continue..")
    elif decision == attr3 or decision == attr4:
        print("no")
        exit()
    else:
        print("sorry i dont understand..pleace try again..")
input_choice("Yes","yes","No","no")

#this will be the block for the second stage but use as example for now.
def first_stage(attr1,attr2,attr3):   
    enter_stage()
    print("Little lamp, sweet and fat, his mothers only _____\n")
    print("1 [proud]\n")
    print("2 [count \n")
    print("3 [pound]\n")

    first_stage = input ("> ")
    if first_stage == attr1:
        print ("Correct!")
    elif first_stage == attr2 or first_stage == attr3:
        print("not correct")

first_stage("1","2","3")
input_choice("Yes","yes","No","no")












   
       



