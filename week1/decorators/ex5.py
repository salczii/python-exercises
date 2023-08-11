from time import time


def timethis(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(end - start)

    return wrapper


@timethis
def big_calc():
    list = []
    for n in range(10000000):
        if n % 2 == 0:
            list.append(n)


big_calc()
