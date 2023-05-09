names = {"Arek","Roman", "Tezeusz", "Klaudiusz" }

numbers = {1, 2, 3, 4, 5}

temperatura = {"t1": -20, "t2": 3, "t3": 15, "t4": -12, "t5": 15}

"""DŁUGOŚĆ STRINGÓW Z WARUNKIEM JEŻELI ZACZYNA SIĘ NA A"""
namesLength = {
                i : len(i)
                for i in names
                if i[0] == "A"
                }


numerMultipled = {
     i : i % 2
     for i in numbers
 }



fahreinheit = {
    klucz : celsjusz * 1.8 + 32
    for klucz, celsjusz in temperatura.items()
}

print(fahreinheit)