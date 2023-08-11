nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_nums = list(filter(lambda squared_num: squared_num % 2 == 0, map(lambda num: num**2, nums)))
print(new_nums)