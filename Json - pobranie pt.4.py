import requests
import json

z = requests.get("https://jsonplaceholder.typicode.com/todos")

"""Uniwersalna funkcja"""


def get_keys_with_top_values(my_dict):
    return [
        print(key)
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]

"""-------------------------------------------------------------------------"""
def completed_tasks(task):
    completed_Tasks_by_user = dict()
    for line in zdecoded_druga_metoda:
        if line["completed"] == True:
            try:
                completed_Tasks_by_user[line["userId"]] += 1
            except KeyError:
                completed_Tasks_by_user[line["userId"]] = 1
    return completed_Tasks_by_user


def usersWithMostCompletedTasks(completed_Tasks_by_user):
    user_id_with_most_completed_tasks = []
    max_amount_completedd_tasks = max(completed_Tasks_by_user.values())
    for userId, number_of_tasks in completed_Tasks_by_user.items():
        if (number_of_tasks == max_amount_completedd_tasks):
            user_id_with_most_completed_tasks.append(userId)
    return user_id_with_most_completed_tasks

try:
    zdecoded_druga_metoda = z.json()

except json.decoder.JSONDecodeError:
    print("Niepoprawny format ")
else:
    completed_Tasks_by_user = completed_tasks(zdecoded_druga_metoda)
    user_with_most_completed_tasks = usersWithMostCompletedTasks(completed_Tasks_by_user)
    print(user_with_most_completed_tasks)


"""=====================DRUGA CZĘŚĆ, PRZYPISANIE ID DO UŻYTKOWNIKÓW=============================="""

users_site_coded = requests.get("https://jsonplaceholder.typicode.com/users")


try:
    users_site_decoded = users_site_coded.json()

except json.decoder.JSONDecodeError:
    print("Niepoprawny format ")
else:
    for line in users_site_decoded:
        for id in user_with_most_completed_tasks:
            if line["id"] == id:
                print(line["name"])


