import time

"""
def function_performance(funkcja, argument):
    funkcja(argument)


def show_message(message):
    print(message)

function_performance(show_message, "Kalafior")

"""
#Funkcje w funkcji

def show_message(message):
    return(message)


def sumujDo(liczba):
    sumaLiczb = 0
    for liczba in range(liczba + 1):
        sumaLiczb += liczba

    return sumaLiczb



def function_performance(funkcja, argument):
    start = time.perf_counter()
    funkcja(argument)
    stop = time.perf_counter()
    return stop - start

print(function_performance(show_message, "Tadam"))
print(function_performance(sumujDo, 5))


