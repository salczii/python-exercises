def fibonacci_generator():
    a = 1
    b = 2
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


gen = fibonacci_generator()


def print_fibonacci(repeats):
    for _ in range(0, repeats):
        print(next(gen))


print_fibonacci(10)
