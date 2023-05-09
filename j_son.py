import json



film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
}


"""ensure asci, aby nie podmieniało znaków specjalnych na znaki z tablicy ASCII"""
"""poniższa komenda zapisuje do stringa/zmiennej"""
"""indent dla lepszej czytelności"""

jasonfilm = json.dumps(film, ensure_ascii= False, indent=4)

print(jasonfilm)

"""następna komenda zapisuje do pliku"""

with open("testowyjson.json", "w", encoding= "UTF-8") as file:
    json.dump(film, file, ensure_ascii= False)


