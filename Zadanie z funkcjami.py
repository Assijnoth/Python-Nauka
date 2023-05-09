import time

def speedTest(funct, argone, argtwo):
    start = time.perf_counter()
    funct(argone, argtwo)
    end = time.perf_counter()
    return(end - start)


def searchEngine(func, search):
    for i in func:
        if search  == i + 1:
            return True
    else:
        return False



setContainer = {i
                for i in range(1000)
                }
listContainer = [i
                 for i in range(1000)
                 ]
print(speedTest(searchEngine, setContainer, 35))
print(searchEngine(setContainer, 1000))




#################################### FUNKCJA SUMUJĄCA WYRAŻENIA ZBIORU

def countEngine(*arg):
    container = [*arg]
    return sum(container)


print(countEngine(1, 2, 3, 5))