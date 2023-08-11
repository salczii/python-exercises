lines = ['10000101011', '111111', '01010101010010', '011001100001', '001010101011']

lists_without_matchword = list(filter(lambda x: x.count('11') == 0, lines))

print(len(lists_without_matchword))
