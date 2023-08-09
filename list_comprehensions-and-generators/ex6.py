three_d = [[[1, 2, 3, 4], [0, -1, -2, -3, -4, -5, -6]], [[1, 10, 15, 12, 20, 20, 20], [-15, -13, 14, 20, -1]]]

filtered_lists = [one_d for two_d in three_d for one_d in two_d if len(one_d) > 4]

print(filtered_lists)


