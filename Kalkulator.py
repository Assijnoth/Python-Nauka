print("KALKULATOR 1.0\n\n")


koniec = "Nie"
liczbaPierwsza = 0
liczbaDruga = 0
rodzajDzialania = 0

while koniec != "STOP":
    liczbaPierwsza = int(input("\nPodaj pierwszą wartość:"))
    liczbaDruga = int(input("\nPodaj drugą wartość:"))
    rodzajDzialania = input("\nJeżeli chcesz dodać wskazane liczby, wpisz: '+' \njeżeli odjąć wpisz '-' \njeżeli mnożyć wpisz '*'\njeśli podzielić '/'.")
    if rodzajDzialania == "+":
        print("\n\nWynikiem dodawania", liczbaPierwsza, "i", liczbaDruga, "jest", liczbaPierwsza + liczbaDruga)
        koniec = input("\nJeśli chcesz przerwać działanie programu wpisz 'STOP'. Aby wykonać kolejną operację wciśnij ENTER")
    elif rodzajDzialania == "-":
        print("\n\nWynikiem odejmowania", liczbaPierwsza, "i", liczbaDruga, "jest", liczbaPierwsza - liczbaDruga)
        koniec = input("\nJeśli chcesz przerwać działanie programu wpisz 'STOP'. Aby wykonać kolejną operację wciśnij ENTER")
    elif rodzajDzialania == "*":
        print("\n\nWynikiem mnożenia", liczbaPierwsza, "i", liczbaDruga, "jest", liczbaPierwsza * liczbaDruga)
        koniec = input("\nJeśli chcesz przerwać działanie programu wpisz 'STOP'. Aby wykonać kolejną operację wciśnij ENTER")
    elif rodzajDzialania == "/":
        print("\n\nWynikiem dzielenia", liczbaPierwsza, "i", liczbaDruga, "jest", liczbaPierwsza / liczbaDruga)
        koniec = input("\nJeśli chcesz przerwać działanie programu wpisz 'STOP'. Aby wykonać kolejną operację wciśnij ENTER")



