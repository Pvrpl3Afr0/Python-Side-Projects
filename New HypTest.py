import random
Done = False
print("Welcome to Henry's Random Number Generator!")
print("I havent' written python in a long time so this thing isn't gonna work.")
print("Anyway, the purpose of this program is to generate random numbers from 1-20 for Hypothesis Testing")
guess = random.randrange(0,21)
complete = 0
while not Done:
    guess = random.randrange(0,21)
    print(guess)
    guess = random.randrange(0,21)
    print(guess)
    complete = complete + 1
    if complete == 50:
        Done = True
        exit
