import json

"""OTWIERANIE ZE STRINGA"""

encoded = '{"title": "Ale ja nie będę tego robił!", "release_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Włodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'



decoded = json.loads(encoded)


print(decoded)



"""OTWIERANIE Z PLIKU"""

with open("testowyjson.json", encoding="UTF - 8") as file:
    encodedfromfile = json.load(file)
    print(encodedfromfile)

"""PRETTY PRINT"""

import pprint
pprint.pprint(encodedfromfile)
