import random
Done = False
print("Welcome to Henry's Random Number Generator!")
print("I havent' written python in a long time so this thing isn't gonna work.")
print("Anyway, the purpose of this program is to generate random numbers from 1-20 for Hypothesis Testing")
minval = int(input("What would you like your minimum value to be?: "))
minval = minval - 1
maxval = int(input("What would you like your maximum value to be?: "))
maxval = maxval - 1
guess = random.randrange(minval,maxval)
complete = 0
while not Done:
    guess = random.randrange(minval,maxval)
    print(guess)
    guess = random.randrange(minval,maxval)
    print(guess)
    complete = complete + 1
    if complete == 50:
        Done = True
        exit
