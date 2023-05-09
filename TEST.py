import requests
import json
import pprint

z = requests.get("https://jsonplaceholder.typicode.com/todos")


zdecoded_druga_metoda = z.json()

x = pprint.pprint(z.json())

try:
    x = pprint.pprint(z.json())
except json.decoder.JSONDecodeError:
    print("Niepoprawny format ")
else:
    completed_Tasks_by_user = dict()
    for line in x:
        if line["completed"] == True:
            completed_Tasks_by_user += 1








try:
    zdecoded_druga_metoda = z.json()

except json.decoder.JSONDecodeError:
    print("Niepoprawny format ")
else:
    completed_Tasks_by_user = dict()
    for line in zdecoded_druga_metoda:
        if line["completed"] == True:
            try:
                completed_Tasks_by_user[line["userId"]] += 1
            except KeyError:
                completed_Tasks_by_user[line["userId"]] = 1
