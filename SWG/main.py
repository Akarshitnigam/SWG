import random

print("Welcome to the SWG game")

def gameWin(comp, you):
    if comp== you:
        return None
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp =='w':
        if you=='s':
            return True
        elif you == 'g':
            return False
    
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
    
    

def game(computerWon, youWon):
 
       print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
       randNo = random.randint(1,3)
       print(randNo)
       if randNo==1:
            comp='s'
       elif randNo== 2:
            comp='w'
       else :
             comp = 'g'

       you= input("Your Turn: Snake(s) Water(w) or Gun(g)?")

       didIWin = gameWin(comp, you)

       if didIWin :
            print("You won !")
            youWon=youWon+1

       else:
           print("Computer won !")
           computerWon +=1

       return computerWon, youWon

'''print("\n")
again=input("Do you wanna try again?").lower()
if again=="yes":
        game()
else:
    quit()
'''







totalNumberOfWins=0
computerWon=0
youWon=0




n = int(input("How many times you wanna play ?"))
while n!=0:
    computerWon, youWon = game(computerWon,youWon)    
    n-=1


print("You won "+str(youWon)+" number of times "+ "and computer won" + " " + str(computerWon)+" "  +"number of times")