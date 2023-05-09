import random


awardValue = {"green": 1000, "orange": 4000, "purple": 9000, "gold": 16000}
movesLeft = 5
turn = 1



def dropchance():
    dropchance = random.randint(1, 100)
    return dropchance

def userAward():
    chestAward = ["green", "orange", "purple", "gold"]
    userAward = random.choices(chestAward, [0.75, 0.20, 0.04, 0.01])
    return userAward

def award():
    temp = userAward()
    temp_Two = temp[0]
    if temp_Two == "green":
        print("Znajdujesz zwykłą skrzynkę ze skarbami!")
        print("W skrzyni znajdujesz", awardValue["green"], "złota.")
    if temp_Two == "orange":
        print("Znajdujesz rzadką skrzynkę ze skarbami!")
        print("W skrzyni znajdujesz", awardValue["orange"], "złota.")
    if temp_Two == "purple":
        print("Znajdujesz epicką skrzynkę ze skarbami!")
        print("W skrzyni znajdujesz", awardValue["purple"], "złota.")
    if temp_Two == "gold":
        print("Znajdujesz legendarną skrzynkę ze skarbami!")
        print("W skrzyni znajdujesz", awardValue["gold"], "złota")



while movesLeft != 0:
    print("Turn", turn, "from 5" )
    if dropchance() >= 60:
        award()
        movesLeft = movesLeft - 1
        turn = turn + 1
        input("Wciśnij enter aby zakończyć grę!")
        continue
    else:
        movesLeft = movesLeft - 1
        turn = turn + 1
        print("Niestety nic nie znalazłeś!")
        input("Wciśnij enter aby zakończyć grę!")
