#Stone paper scissor game

import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'p':
            return True
        elif you == 'c':
            return False    
    elif comp == 'p':
        if you == 's':
            return False
        elif you == 'c':
            return True    
    elif comp == 'c':
        if you == 's':
            return True
        elif you == 'p':
            return False    

print("Computer turn: stone(s), paper(p), scissor(c)")
randomno = random.randint(1, 3)
if randomno == 1:
    comp = 's'
elif randomno == 2:
    comp = 'p'
elif randomno == 3:
    comp = 'c'

you = input("Your turn select: stone(s), paper(p), scissor(c) : ")

print(f"Computer choose '{comp}'")
print(f"You choose '{you}'")


a = gamewin(comp, you)
if a == None:
    print("The Game is tie")
elif a == True:
    print("You won the game")    
elif a == False:
    print("You loss the game")    


