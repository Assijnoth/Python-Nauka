lista = [1, 2, 3, 4, 5]

#Lambda

lista2 = list(filter(lambda x: x % 2 == 0, lista))

#Wyrażenie listowne

lista3 = [i
          for i in lista
          if (i % 2 == 0)]

#Definicja

def podzielnik(x):
    for i in x:
        if i % 2 == 0:
            print(i)
    return




print(podzielnik(lista))
