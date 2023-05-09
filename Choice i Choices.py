"""
choice - zwraca losowy element
choices - zwraca listę elementów i ma większe możliwości
counter - zlicza ile razy zwrócono dany element/elementy
"""

import random

movieList = ["Tytuł 1", "Tytuł 2", "Tytuł 3", "Tytuł 4"]

event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata życia", "losowa rzecz"]

nagrodaZeSkrzynki = ["zielona", "pomarańczowa", "fioletowa", "złota"]

from collections import Counter

print(Counter(random.choices(movieList, k=1000)))

print(Counter(random.choices(nagrodaZeSkrzynki, [0.8, 0.15, 0.04, 0.01], k = 100)))

print(Counter(random.choices(event, [7, 1, 0.5, 0.5, 0.5, 0.5], k = 1000)))
