import random
import time

playerlist = []

print("Welcome to Pvrple's Bracket Generator! Here, you can create a \
text based bracket for whatever purpose you may need. First, \
Let's start with the names.")
done = 0
vs = int(input("How many players are there? Please input a number: "))
MU = 0 #Matchups
while done < vs:
    players = input("Player Name: ")
    playerlist.append(players)
    done = done + 1
print(playerlist)
print("Now, let's match these players up against eachother.")
while MU < vs:
    time.sleep(1)
    print("one moment please...")
    time.sleep(1)
    playerA = random.choice(playerlist)
    print(playerA, "vs")
    playerlist.remove(playerA)
    playerB = random.choice(playerlist)
    print(playerB)
    playerlist.remove(playerB)
    MU = MU + 2
