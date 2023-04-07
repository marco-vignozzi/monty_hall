import random as r
import timeit


def init_doors(token):               # randomly initializes the doors contents depending on the token
    if token == 0:
        doors = ["sheep", "sheep", "car"]
    elif token == 1:
        doors = ["sheep", "car", "sheep"]
    else:
        doors = ["car", "sheep", "sheep"]
    return doors


def choose_door(doors):                     # randomly chooses a door
    pick = r.randrange(0, 1001) % 3
    # print(f"You pick the door {pick + 1}")
    return pick


def open_door(doors, pick):                 # opens the first door that hasn't been chosen and is hiding a sheep
    for i in range(0, 3):
        if doors[i] == "sheep" and i != pick:
            doors[i] = "open"
            return doors


def change_pick(doors, pick):               # changes the door's choice with the one that hasn't been opened
    for i in range(0, 3):
        if doors[i] != "open" and i != pick:
            new_pick = i
            return new_pick


attempts = 100000              # number of times that the test is repeated
wins = 0                        # stores the wins number
loss = 0                        # stores the loss number

while attempts != 0:

    token = r.randrange(0, 1001) % 3
    # print(f"Token: {token}")
    doors = init_doors(token)
    # print(doors)

    pick = choose_door(doors)
    doors = open_door(doors, pick)
    new_pick = change_pick(doors, pick)

    if doors[new_pick] == "car":
        # print("You win a brand-new car!")
        wins += 1
    else:
        loss += 1
        # print("You loose, unlucky :(")

    del doors
    attempts -= 1

print(f"You win {wins} times\nYou loose {loss} times\n")
