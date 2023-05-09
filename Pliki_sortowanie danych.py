namesandsurnames = []

with open("imionanazwiska.txt", "r", encoding= "UTF - 8") as file:
    for line in file:
        namesandsurnames.append(line.replace("\n", "").split())




with open("imiona.txt", "w", encoding= "UTF - 8") as file:
    for element in namesandsurnames:
        file.write(element[0] + "\n")

with open("nazwiska.txt", "w", encoding= "UTF - 8") as file:
    for element in namesandsurnames:
        if len(element) == 2:
            file.write(element[1] + "\n")
        else:
            file.write("\n")

