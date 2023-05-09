import sys
"""Wykorzystujemy generatory,  gdy pobieramy bardzo dużo informacji
i niekoniecznie chcemy na tych danych wykonywać operacje"""
numery = [i
          for i in range(400)
          if (i % 2 == 0)
          ]


##Zajmuje o wiele mniej pamięci - GENERATOR
"""
numeryDwa = (i
          for i in range(400)
          if (i % 2 == 0)
             )


for i in numeryDwa:
    print(i)
    
"""


numerTrzy = (i ** 2
             for i in range(101)
             )


print(sys.getsizeof(numerTrzy))


