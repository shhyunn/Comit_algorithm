from itertools import combinations_with_replacement
lst = [1,2,3,4,5]

for lst in combinations_with_replacement(lst,3):
    print(lst)
