import random


cards = ["Jack","King", "Queen", "Ace", "Joker"]


def shufflecards(list, x):
    random.shuffle(list)
    red = []
    blue = []
    for i in range(x):
        temp = list.pop()
        red.append(temp)
        temp = list.pop()
        blue.append(temp)
    print("Blue", blue)
    print("Red", red)
    print(cards)



shufflecards(cards, 2)



