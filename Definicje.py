"""

def powitanie(imie):
    print("Witaj", imie, "w naszym newsletterze!")


imiona = ["Arek", "Sławek"]

imieuz = input("Jak Ci na imię?")

powitanie(imieuz)

"""

"""
def pole_prostokata(a, b):
    return a * b


a = pole_prostokata(2, 5)

print(a)

"""


def dzielenie(x, y):
    if (y == 0):
        return
    if x == 0:
        return
    return x / y


if dzielenie(9, 3):
    print("Wynik to:", dzielenie(1, 2))
else:
    print("Nie dziel przez zero!")




