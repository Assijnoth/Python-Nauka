import requests


working_sites = []
not_working_sites = []

with open("strony.txt", "r") as file:
    for line in file:
        site = requests.get(line)
        if site.status_code == 200:
            working_sites.append(line.replace("\n", ""))
        else:
            print("No")



print(working_sites)