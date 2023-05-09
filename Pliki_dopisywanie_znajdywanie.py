with open("kontynenty.txt", "a+") as file:
    file.write("Europa\n")
    file.write("Azja\n")
    file.write("Afryka")
    print(file.tell())
