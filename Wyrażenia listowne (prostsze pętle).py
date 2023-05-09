lista = [2, 5, 1, 7, 8]

potegaDwojki = []
for i in lista:
    potegaDwojki.append(i**2)

###LUB

potegaDwojkiDwa = [i**2
                   for i in lista
                    ]






###=====================================





liczbyparzyste = []
for i in lista:
    if (i % 2 ==0):
        liczbyparzyste.append(i)

###LUB

liczbyparzysteDwa = [i
                     for i in lista
                     if (i % 2 == 0)
                     ]


print(liczbyparzysteDwa)
print(potegaDwojkiDwa)
