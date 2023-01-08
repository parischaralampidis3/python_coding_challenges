#import time modules
import time as t

def set_timer():
    print("set preffered seconds.. ")
    seconds =int(input('> '))
    print ("preffered seconds: %s " % seconds)
    
    print("Your timer is going to begin..Ready?")
    t.sleep(3)
#LOOP THROUGH  NUMBERS 

    for i in range(seconds):
        print("remaining seconds: " +str(seconds-i ),end='\n \r')
        t.sleep(2)
set_timer()

print("Happy new Year!")



