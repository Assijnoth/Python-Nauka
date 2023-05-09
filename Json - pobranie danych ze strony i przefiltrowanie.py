import requests
import json

z = requests.get("https://jsonplaceholder.typicode.com/todos")

"""

zdecoded = json.loads(z.text)
"""

"""metoda krótsza, ponadto sama sprawdza czy zwraca jsona"""



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


    """wybranie największej wartości ze słownika, konwersja dictionary w krotki i zestawienie wartości w celu wyłonienia największych"""
    user_id_with_most_completed_tasks = []
    max_amount_completedd_tasks = max(completed_Tasks_by_user.values())
    for userId, number_of_tasks in completed_Tasks_by_user.items():
        if (number_of_tasks == max_amount_completedd_tasks):
            user_id_with_most_completed_tasks.append(userId)


