imiona = {"arek", "Tomek", "Wiola", "beata"}

imiona = {i.capitalize()
          for i in imiona
          if i[0] == "a"
          }

print(imiona)