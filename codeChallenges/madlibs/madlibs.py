#score fuctionality
score = 0 
def showScore():
    global score
    score = score+10
    print(score)
showScore()

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

#this is the main block function,for the first the question challenge for the game.
def first_stage(attr1,attr2,attr3):   
    print("Little lamp, sweet and fat, his mothers only _____\n")
    print("1 [proud]\n")
    print("2 [count] \n")
    print("3 [pound]\n")
    
    first_stage = input ("> ")
    if first_stage == " ":
        print("Sorry, i dont understand")
        exit(0)
    elif first_stage == attr1:
        print ("Correct!")
        showScore()
    elif first_stage == attr2 or first_stage == attr3:
        print("not correct")
    else:
        print("sorry i don't understand")
        exit(0)
    
first_stage("1","2","3")

#validate the choice of the user
def input_choice(attr1,attr2,attr3,attr4):    
    print("Are you ready to continue?\n")
    print("Type Yes/yes for yes, or No/no for no, to continue..")
    decision = input("> ")
    print(decision)
    if decision == attr1 or decision == attr2:
         print("Please continue..")
    elif decision == attr3 or decision == attr4:
        print("no")
        exit(0)
    else:
        print("sorry i dont understand..pleace try again..")
input_choice("Yes","yes","No","no")

#this is the main block function,for the second the question challenge for the game.
def second_stage(attr1,attr2,attr3):   
    enter_stage()
    print("The early bird catches the _______\n")
    print("1 [storm]\n")
    print("2 [worm] \n")
    print("3 [norm]\n")

    second_stage = input ("> ")
    if second_stage == " ":
        print("Sorry, i dont understand")
        exit(0)
    elif second_stage == attr1 or second_stage == attr3:
        print ("Not Correct!")
    elif second_stage == attr2:
        print("Correct")
        showScore()
    else:
        print("sorry i don't understand")
        exit(0)
second_stage("1","2","3")
input_choice("Yes","yes","No","no")

#this is the main block function,for the third the question challenge for the game.
def third_stage(attr1, attr2, attr3):
    enter_stage()
    print("Dont count your ________ before they hatch\n")
    print("1 [pigs]\n")
    print("2 [hens] \n")
    print("3 [chickens]\n")

    third_stage = input("> ")
    if third_stage == " ":
        print("Sorry, i dont understand")
        exit(0)
    elif third_stage == attr3:
        print("Correct")
        showScore()
    elif third_stage == attr1 or third_stage == attr2:
        print("Not correct")
    else:
        print("sorry i don't understand")
        exit(0)
third_stage("1","2","3")
input_choice("Yes","yes","No","no")

#this is the main block function,for the fouth question challenge for the game.
def fourth_stage(attr1, attr2, attr3):
    enter_stage()
    print("Kill two birds with one ______\n")
    print("1 [stone]\n")
    print("2 [gun] \n")
    print("3 [stick]\n")

    fourth_stage = input("> ")
    if fourth_stage == " ":
        print("Sorry, i dont understand")
        exit(0)    
    elif fourth_stage == attr1:
        print("Correct")
        showScore()
    elif fourth_stage == attr2 or fourth_stage == attr3:
        print("Not correct")
    else:
        print("sorry i don't understand")
        exit(0) 
fourth_stage("1","2","3")
input_choice("Yes","yes","No","no")

#this is the main block function,for the fifth question challenge for the game.
def fifth_stage(attr1, attr2, attr3):
    enter_stage()
    print("It costs an arm and a ______\n")
    print("1 [leg]\n")
    print("2 [head] \n")
    print("3 [hand]\n")

    fifth_stage = input("> ")
    if fifth_stage == " ":
        print("Sorry, i dont understand")
        exit(0)
    elif fifth_stage == attr1:
       
        print("Correct, " + "your score is: \n")
        showScore()
        print("Thanks for playing! \n")
    elif fifth_stage == attr2 or fourth_stage == attr3:
        print("Not correct")
    else:
        print("sorry i don't understand")
        exit(0) 
fifth_stage("1","2","3")






















   
       



