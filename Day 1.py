from itertools import combinations

def checkcombinations(mylist, mynumber):
    l = list(combinations(mylist, 2))
    for i in l:
        if sum(i) == mynumber:
            return True
    return False

i = checkcombinations([10,15,3,7],21)
print(i)
