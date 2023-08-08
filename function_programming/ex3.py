def square_and_cube(numbers):
    squares = list(map(lambda x: x ** 2, numbers))
    cubes = list(map(lambda x: x ** 3, numbers))
    return squares, cubes


squares, cubes = square_and_cube([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(squares, cubes)

