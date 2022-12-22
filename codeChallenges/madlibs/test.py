"""
score = 0 

def showScore():
    global score
    score = score+5
    print(score)

showScore()
showScore()
"""
def score(change, old_score=0):
    new_score = old_score + change
    print(new_score)
    return new_score
 
x = score(6)
x = score(1, x)
