import requests

def is_site_on (sitename):
    site = requests.get(sitename)
    print(site)
    print(type(site))
    if site == "status_code == 200":
        print("Strona odnaleziona")
    else:
        print("Nie odnaleziono strony")


is_site_on("https://www.facebook.com/")




"""======================================================="""
"""ECOMHOUSE"""

def test_is_site_on (sitename):
    onsites = []
    offsites = []
    wrongsites = []
    try:
        site = requests.get(sitename)
        if site.status_code == 200:
            onsites.append(sitename)
        elif site.status_code == 404:
            offsites.append(sitename)
        else:
            offsites.append(sitename)
    except requests.exceptions.ConnectionError:
        wrongsites.append(sitename)


    return print("Strony działające:", onsites, "strony niedziałające", offsites)

test_is_site_on("https://www.mdsforele.net/p-2/sdf")