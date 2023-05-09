from heapq import merge

defiTemp = {}
defFinal = {}
koniec = (" ")
menu = ("START")

print("Program 'SŁOWNIK' pozwala na dodawanie kluczy i definicji wskazanych przez użytkownika, oraz zarządzanie nimi\n")

while menu != "STOP":
    menu = input(print("\nWybierz polecenie do wykonania:", "\n 1 - dodaj nową definicję do słownika",
                       "\n 2 - wyszukaj definicję","\n 3 - usuń wskazaną definicję", "\n 4 - zakończ działanie programu"))
    if menu == "1":
        for i in range(3):
            klucz = input("Podaj klucz: ")
            definicja = input("Podaj definicję: ")
            defiTemp[klucz] = definicja
            defFinal = defiTemp | defFinal
            print("\nDefinicja dodana pomyślnie do słownika!")
            koniec = input("\nJeśli chcesz przerwać działanie programu wpisz 'STOP'. \nAby powrócić do menu, wciśnij dowolny klawisz'")
            if koniec == "DALEJ":
                break
            elif koniec == "STOP":
                input("Wciśnij dowolny klawisz aby zakończyć")
                menu = "STOP"
                break
            else:

                break
    elif menu == "2":
        klucz = input("Jakiego słowa szukasz?")
        if klucz in defFinal:
            print("\n\nDefinicją słowa", klucz, "jest:", defFinal[klucz], "\n\n")
        else:
            print("\n\nNie ma takiego słowa w słowniku!\n\n")
            continue
    elif menu == "3":
        klucz = input("\nKtóry klucz chcesz usunąć ze słownika?\n")
        defFinal.pop(klucz)
        print("Klucz", klucz, "został usunięty ze słownika!")
    elif menu == "4":
        menu = "STOP"
        input("Wciśnij dowolny klawisz aby zakończyć działanie programu")
        break
    else:
        print("\nWprowadziłeś błędną wartość, spróbuj ponownie!\n")


##TEST







