def count(func):
    function_count = {}

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        if func.__name__ not in function_count:
            function_count[func.__name__] = 1
        else:
            function_count[func.__name__] += 1
        print(f"{func.__name__} was called {function_count[func.__name__]} times")

    return wrapper


@count
def sum_numbers(a, b):
    return a + b


@count
def multiply_numbers(a, b):
    return a * b


sum_numbers(1, 2)
multiply_numbers(1, 2)
sum_numbers(1, 2)
sum_numbers(1, 2)
multiply_numbers(1, 2)
