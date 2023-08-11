import traceback


class MyStopIteration(Exception):
    pass


def func():
    for i in range(10):
        yield i
    raise MyStopIteration("throw an exception")


gen = func()

try:
    gen.__next__()
    gen.__next__()
    gen.__next__()
    gen.__next__()
    gen.__next__()
    gen.__next__()
    for val in gen:
        print(val)


except MyStopIteration as e:
    print("Generator end its work:", e)
    traceback.print_exc()
