"""Stwórz menu, z którego użytkownik, może wybrać opcje, aby policzyć powierzchnie figur:

1) prostokąta
2) kwadratu
3) trójkąta
4) trapezu
5) koła
Pamiętaj, by skorzystać z funkcji."""

import math
from enum import IntEnum

Menu_Figury = IntEnum("Menu", "Prostokąt, Kwadrat, Trójkąt, Trapez, Koło")


def pole_prostokata(a, b):
    if a == 0:
        return
    if b == 0:
        return
    return a * b

def pole_kwadratu(a):
    if a == 0:
        return
    return a ** 2

def pole_trojkata(a, h):
    if a == 0:
        return
    if h == 0:
        return
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    if a == 0:
        return
    if b == 0:
        return
    if h == 0:
        return
    return (a + b) / 2 * h

def pole_kola(p):
    if p == 0:
        return
    return math.pi * p ** 2

print("Witaj w programie obliczającym pole powierzchni figur geometrycznych!\n")
menu = int(input("Pole jakiej figury chciałbyś obliczyć? Wybierz 1 - prostokąt, 2 - kwadrat, 3 - trójkąt, 4 - trapez, 5 - koło. Aby zakończyć działanie programu wpisz '0' "))

while menu != 0:
    if menu == Menu_Figury.Prostokąt:
        a = int(input("Wprowadź długość pierwszego boku prostokąta "))
        b = int(input("Wprowadź długość drugiego boku prostokąta "))
        if pole_prostokata(a, b):
            print("\nPole prostokąta wynosi", pole_prostokata(a, b))
            menu = int(input("Pole jakiej figury chciałbyś obliczyć? Wybierz 1 - prostokąt, 2 - kwadrat, 3 - trójkąt, 4 - trapez, 5 - koło. Aby zakończyć działanie programu wpisz '0' "))
        else:
            print("Wprowadziłeś nieprawidłowe wartości!\n")

    if menu == Menu_Figury.Kwadrat:
        a = int(input("Wprowadź długość dowolnego boku kwadratu "))
        if pole_kwadratu(a):
            print("\nPole kwadratu wynosi", pole_kwadratu(a))
            menu = int(input("Pole jakiej figury chciałbyś obliczyć? Wybierz 1 - prostokąt, 2 - kwadrat, 3 - trójkąt, 4 - trapez, 5 - koło. Aby zakończyć działanie programu wpisz '0' "))
        else:
            print("Wprowadziłeś nieprawidłowe wartości!\n")
    if menu == Menu_Figury.Trójkąt:
        a = int(input("Wprowadź długość podstawy trójkąta "))
        h = int(input("Wprowadź wysokość trójkąta "))
        if pole_trojkata(a, h):
            print("\nPole trójkąta wynosi", pole_trojkata(a, h))
            menu = int(input("Pole jakiej figury chciałbyś obliczyć? Wybierz 1 - prostokąt, 2 - kwadrat, 3 - trójkąt, 4 - trapez, 5 - koło. Aby zakończyć działanie programu wpisz '0' "))
        else:
            print("Wprowadziłeś nieprawidłowe wartości!\n")
    if menu == Menu_Figury.Trapez:
        a = int(input("Wprowadź długość pierwszego boku trapezu "))
        b = int(input("Wprowadź długość drugiego boku trapezu "))
        h = int(input("Wprowadź wysokość trapezu "))
        if pole_trapezu(a, b, h):
            print("\nPole trapezu wynosi", pole_trapezu(a, b, h))
            menu = int(input("Pole jakiej figury chciałbyś obliczyć? Wybierz 1 - prostokąt, 2 - kwadrat, 3 - trójkąt, 4 - trapez, 5 - koło. Aby zakończyć działanie programu wpisz '0' "))
        else:
            print("Wprowadziłeś nieprawidłowe wartości!\n")
    if menu == Menu_Figury.Koło:
        p = int(input("Wprowadź promień koła "))
        if pole_kola(p):
            print("\nPole koła wynosi", pole_kola(p))
            menu = int(input("Pole jakiej figury chciałbyś obliczyć? Wybierz 1 - prostokąt, 2 - kwadrat, 3 - trójkąt, 4 - trapez, 5 - koło. Aby zakończyć działanie programu wpisz '0' "))
        else:
            print("Wprowadziłeś nieprawidłowe wartości!\n")
