#LISTY
print("LISTY")

a = [2, 1, 6, 7, 8, "kalafior"]
b = [5, 3, 1, 2]
c = a + b
print(a)
print(a + b)

len(a) # długość
a.append("ogórek")  # dodanie elementu na koniec
a.insert(2, "wiatrak") #wstawić
podKtorym = a.index("kalafior") #pod którym indeksem

print("\n\n", a)
print(podKtorym)
print(len(a))

##KROTKI
print("\n\n\n\n\nKROTKI")

d = 4, 5 ,6
e = 7, 9, 3

print(d + e)

##ZBIORY
print("\n\n\n\n\nZBIORY")

A = {1, 4, 20, -4, 20, 1}
C = {35, 42, 20, -42, 203, 1}
A.add(7)  #dodaje do zbioru 7
print(A&C)  #zostawi wspólne elementy
A.discard(-4)   #wyrzuci element -4 ze zbioru

B = [1, 4, 1, 20, 54]
print(set(A))    ##przekształci listę w zbiór (i przy okazji usunie duplikaty)

print(A|C)  #doda oba zbiory, usunie duplikaty


print(A-C)  #zostawia elementy A nie bedace w zbiorze C
print(A^C)  #alternatywa wykluczająca zostawia to,co nie jest wspólne