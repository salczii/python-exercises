def is_prime(n):
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


gen = prime_generator()


def print_prime_numbers(number):
    for _ in range(0, number):
        print(next(gen))


print_prime_numbers(10)
