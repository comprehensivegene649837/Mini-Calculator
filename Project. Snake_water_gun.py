import os
import random
def game(you, comp):
    if comp==you:
        return None
    elif comp== 's':
        if you== 'w':
            return False
        elif you== 'g':
            return True
    elif comp == 'w':
        if you== 'g':
            return False
        elif you== 's':
            return True
    elif comp=='g':
          if you== 's':
              return False
          elif you== 'w':
                return True

print("computer's turn : snake(s), water(w), gun(g): ")
#print(input("computer's turn : snake(s), water(w), gun(g)"))
randonN= random.randint(1, 3) #this means 1 to 3
#print(comp, randonN)
if randonN==1:
    comp= 's'
elif randonN==2:
    comp= 'w'
elif randonN==3:
    comp= 'g'

you = (input("your turn: "))

a= game(you, comp)

print(f'computer chose: {comp}')
print(f'you chose: {you}')


if a ==None:
    print("the game is tie")
elif a:
    print("you win! ")

else:
    print("you lost!")



os.system("pause")

#b= input("your turn: snake(1), water(2), gun(3)"