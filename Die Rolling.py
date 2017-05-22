#Dice Roller for Chi-Squared testing

import random
Done = False

if Done == True:
    exit


print("Welcome to my Dice Simulator!")
print("The purpose of this program is to simulate rolling a six sided die for the purpose of Chi-Squared testing")

sides = int(input("How many sides would you like on your die?: "))
sides = int(sides + 1)
num = random.randrange(1 , sides)
while not Done:
    roll = input("Would you like to Roll or Quit?: ")
    if roll == "roll" or roll =="Roll":
        print("You landed a...", num)
        num = random.randrange(1 , sides)
        Done = False
    elif roll == "quit" or roll == "Quit":
        print("Thanks for rolling!")
        Done = True
    else:
        print("Something went wrong!")
