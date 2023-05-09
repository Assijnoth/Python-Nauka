import time

def speedTest(x, y, r, w):
    start = time.perf_counter()
    x(y, r, w)
    end = time.perf_counter()
    print(end - start)



def testowaDefinicja(x):
    for i in range(x):
        return(i)


def drugaDefinicja(x, y, r):
    return x + y * r


speedTest(drugaDefinicja, 24, 54, 1)



