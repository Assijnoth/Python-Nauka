import random
from enum import IntEnum




print("Podążając szlakiem pod osłoną nocy, dostrzegasz naprzeciw siebie zarys olbrzymiej humanoidalnej sylwetki... \n...unosisz rozpaloną pochodnię przed siebie i dostrzegasz, że owy zarys to ork.\n",
      "\nDysponujesz mieczem, eliksirem życia, zwojem redukcji pancerza oraz Młotem Ogłuszenia.",
      "\nBroń się!\n\n\n")


menu = IntEnum("menu", "Miecz, Młot, Zwój, Eliksir")


turnCounter = 1
print("                     ===========================Tura", turnCounter, "============================")
menuChoice = int(input("""                     ==============================================================\n\n
                Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))

def enemyMiss():
    missText = ["Topór orka ociera się ledwie o krawędź Twojego pancerza. Pudłuje!",
                "Ork źle dobrał odległość ataku i jego cios wymierzony został w pustą przestrzeń. Pudło!",
                "Ork stracił koordynację przy wyprowadzaniu ciosu i pudłuje!",
                "Twój pancerz z łatwością przyjmuje nieprecyzyjnie wymierzony cios orka!",
                "Miejsce, w które trafia ork okazuje się zbyt mocne względem wyprowadzonego ciosu!"  ]

    print(random.choice(missText))
    return hpInfo()



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

def userMiss():
    missType = random.randrange(1, 6)
    if missType == 1:
        print("Broń wyślizguje Ci się z dłoni, przez co Twój atak jest nieskuteczny!")
    elif missType == 2:
        print("Twoja stabilizacja uległa zawahaniu w trakcie ataku - pudłujesz!")
    elif missType == 3:
        print("Twoja broń osuwa się równolegle do płaszczyzny pancerza orka. Pudłujesz!!")
    elif missType == 4:
        print("Źle obliczyłeś odległość od orka. Twój atak jest przestrzelony!")
    else:
        print("Nic z tego! Pancerz orka jest zbyt mocny!")
    return



userHP = 50
userArmor = 50
userSword = random.randrange(2, 11)
userScrool = random.randrange(10, 25)
userScroolCount = 1
userPotion = random.randrange(10, 25)
userPotionCount = 1
userSwordTempDamage = 0
userMaceTempDamage = 0
enemyTempDamage = 0

enemyHP = 80
enemyArmor = 50
enemyWeapon = random.randrange(1, 10)


def hpInfo():
    print("\nAktualnie masz", userHP, " punktów życia i ", userArmor, "punktów pancerza","\nOrk ma", enemyHP, "punktów życia i", enemyArmor, "punktów pancerza (", 100 - enemyArmor, "% szans na trafienie)")

def userAttack():
    print("Wykonujesz atak mieczem, trafiasz przeciwnika i zadajesz", userSwordTempDamage, "obrażeń orkowi!\n")


def userAttackMace():
    print("Wykonujesz atak młotem, trafiasz przeciwnika i zadajesz", userMaceTempDamage, "obrażeń orkowi!\n")


def enemyAttack():
    print("Przeciwnik atakuje Cię toporem, i zadaje Ci", enemyTempDamage, "obrażeń!\n")


def hitChance():
    hitvalue = random.randrange(1, 100)
    print("\nTwój rzut na przebicie pancerza wyniósł", hitvalue)
    return hitvalue

def hitChance2():
    hitvalue = random.randrange(1, 100)
    print("\nPrzeciwnik wyrzuca", hitvalue)
    return hitvalue

def enemyDamage():
    global enemyTempDamage
    enemyTempDamage = random.randrange(1, 11)
    return enemyTempDamage

def userSwordDamage():
    global userSwordTempDamage
    userSwordTempDamage = random.randrange(1, 11)
    return userSwordTempDamage

def userMace():
    global userMaceTempDamage
    userMaceTempDamage = random.randrange(1, 5)
    return userMaceTempDamage

def userStun():
    stun = random.randrange(1, 100)
    print("Twój rzut na ogłuszenie wyniósł", stun)
    return stun






while menu != 5:
    ### ATAK MIECZEM ###
    if menuChoice == menu.Miecz:
        if hitChance() >= enemyArmor:
            userSwordDamage()
            userAttack()
            enemyHP = enemyHP - userSwordTempDamage
            if enemyHP > 0:
                if hitChance2() >= userArmor:
                    enemyDamage()
                    enemyAttack()
                    userHP = userHP - enemyTempDamage
                    if userHP > 0:
                        hpInfo()
                        turnCounter += 1
                        print("\n\n                         ===========================Tura", turnCounter, "============================")
                        menuChoice = int(input("""                         ==============================================================\n\n
                Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))

                    else:
                        input("Zginąłeś! Koniec gry!")
                        break
                else:
                    enemyMiss()
                    turnCounter += 1
                    print("\n\n                         ===========================Tura", turnCounter, "============================")
                    menuChoice = int(input("""                         ==============================================================\n\n
                Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))
            else:
                hpInfo()
                input("\n\nWielkie ciało orka osuwa się na ziemię. Zwyciężyłeś!")
                while True:
                    print("\nPrzeszukujesz truchło przeciwnika.\n")
                    if dropchance() >= 60:
                        award()
                        movesLeft = movesLeft - 1
                        turn = turn + 1
                        input("Wciśnij enter aby zakończyć grę!")
                        break
                    else:
                        movesLeft = movesLeft - 1
                        turn = turn + 1
                        print("Niestety nic nie znalazłeś!")
                        input("Wciśnij enter aby zakończyć grę!")
                        break
                break
        else:
            userMiss()
            if hitChance2() > userArmor:
                enemyDamage()
                enemyAttack()
                userHP = userHP - enemyTempDamage
                if userHP > 0:
                    hpInfo()
                    turnCounter += 1
                    print("\n\n                         ===========================Tura", turnCounter, "============================")
                    menuChoice = int(input("""                         ==============================================================\n\n
                Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))
                else:
                    input("Zginąłeś! Koniec gry!")
                    break

            else:
                enemyMiss()
                turnCounter += 1
                print("\n\n                         ===========================Tura", turnCounter, "============================")
                menuChoice = int(input("""                         ==============================================================\n\n
                Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))
    ###MŁOT###
    if menuChoice == menu.Młot:
        if hitChance() >= enemyArmor:
            userMace()
            userAttackMace()
            enemyHP = enemyHP - userMaceTempDamage
            if enemyHP > 0:
                if userStun() > 50:
                    print("Udało Ci się ogłuszyć przeciwnika!")
                    hpInfo()
                    turnCounter += 1
                    print("\n\n                         ===========================Tura", turnCounter, "============================")
                    menuChoice = int(input("""                         ==============================================================\n\n
                    Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                    Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                    Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                    Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))

                else:
                    print("Nie udało Ci się ogłuszyć wroga!")
                    if hitChance2() >= userArmor:
                        enemyDamage()
                        enemyAttack()
                        userHP = userHP - enemyTempDamage
                        if userHP > 0:
                            hpInfo()
                            turnCounter += 1
                            print("\n\n                         ===========================Tura", turnCounter, "============================")
                            menuChoice = int(input("""                         ==============================================================\n\n
                    Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                    Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                    Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                    Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))

                        else:
                            input("Zginąłeś! Koniec gry!")
                            break
                    else:
                        enemyMiss()
                        turnCounter += 1
                        print("\n\n                         ===========================Tura", turnCounter, "============================")
                        menuChoice = int(input("""                         ==============================================================\n\n
                    Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                    Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                    Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                    Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))


            else:
                hpInfo()
                input("\n\nWielkie ciało orka osuwa się na ziemię. Zwyciężyłeś!")
                while True:
                    print("\nPrzeszukujesz truchło przeciwnika.\n")
                    if dropchance() >= 60:
                        award()
                        movesLeft = movesLeft - 1
                        turn = turn + 1
                        input("Wciśnij enter aby zakończyć grę!")
                        break
                    else:
                        movesLeft = movesLeft - 1
                        turn = turn + 1
                        print("Niestety nic nie znalazłeś!")
                        input("Wciśnij enter aby zakończyć grę!")
                        break
                break
        else:
            userMiss()
            if hitChance2() > userArmor:
                enemyDamage()
                enemyAttack()
                userHP = userHP - enemyTempDamage
                if userHP > 0:
                    hpInfo()
                    turnCounter += 1
                    print("\n\n                         ===========================Tura", turnCounter, "============================")
                    menuChoice = int(input("""                         ==============================================================\n\n
                Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))
                else:
                    input("Zginąłeś! Koniec gry!")
                    break

            else:
                enemyMiss()
                turnCounter += 1
                print("\n\n                         ===========================Tura", turnCounter, "============================")
                menuChoice = int(input("""                         ==============================================================\n\n
                Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))

    if menuChoice == menu.Zwój:
        if userScroolCount > 0:
            enemyArmor = enemyArmor - userScrool
            userScroolCount = userScroolCount - 1
            print("\nRzucasz zaklęcie ze zwoju i uszkadzasz pancerz przeciwnika o ", userScrool, "punktów!")
            if hitChance2() > userArmor:
                enemyDamage()
                enemyAttack()
                userHP = userHP - enemyTempDamage
                if userHP > 0:
                    hpInfo()
                    turnCounter += 1
                    print("\n\n                         ===========================Tura", turnCounter, "============================")
                    menuChoice = int(input("""                         ==============================================================\n\n
                Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))
                else:
                    input("Zginąłeś! Koniec gry!")
                    break
            else:
                enemyMiss()
                turnCounter += 1
                print("\n\n                         ===========================Tura", turnCounter, "============================")
                menuChoice = int(input("""                         ==============================================================\n\n
                Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))

        else:
            print("\n\nWykorzystałeś już zwój uszkodzenia pancerza!")
            print("\n\n                         ===========================Tura", turnCounter, "============================")
            menuChoice = int(input("""                         ==============================================================\n\n
                Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))

    if menuChoice == menu.Eliksir:
        if userPotionCount > 0:
            userHP = userHP + userPotion
            userPotionCount = userPotionCount - 1
            print("\nWypijasz eliksir życia, który przywraca Ci ", userPotion, "punktow zdrowia")
            if hitChance2() > userArmor:
                enemyDamage()
                enemyAttack()
                userHP = userHP - enemyTempDamage
                if userHP > 0:
                    hpInfo()
                    turnCounter += 1
                    print("\n\n                         ===========================Tura", turnCounter, "============================")
                    menuChoice = int(input("""                         ==============================================================\n\n
                Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))
                else:
                    input("Zginąłeś! Koniec gry!")
                    break
            else:
                enemyMiss()
                turnCounter += 1
                print("\n\n                         ===========================Tura", turnCounter, "============================")
                menuChoice = int(input("""                         ==============================================================\n\n
                Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))

        else:
            print("\n\nWykorzystałeś już eliksir życia!")
            print("\n\n                         ===========================Tura", turnCounter, "============================")
            menuChoice = int(input("""                         ==============================================================\n\n
                Aby zaatakować mieczem (obrażenia od 1 - 10) wybierz 1, 
                Aby zaatakować młotem (obrażenia od 1 - 4 i 50% szans na ogłuszenie) wybierz 2, 
                Aby użyć zwój uszkadzający pancerz (od 10 - 25) wybierz 3,
                Aby wypić miksturę życia (przywraca od 10 - 25 pkt. życia) wybierz 4  """))










