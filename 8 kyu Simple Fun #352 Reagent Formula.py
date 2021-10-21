# 8 kyu
# Simple Fun #352: Reagent Formula

def isValid(formula):
    cnt = 0

    if (1 in formula and 2 not in formula) or (2 in formula and 1 not in formula):
        cnt += 1
    if (3 in formula and 4 not in formula) or (4 in formula and 3 not in formula):
        cnt += 1
    if 5 and 6 in formula:
        cnt += 1
    if (7 in formula or 8 in formula) or (7 and 8 in formula):
        cnt += 1

    return cnt


print(isValid([1, 3, 7]), True)
print(isValid([7, 1, 2, 3]), False)
print(isValid([1, 3, 5, 7]), False)
print(isValid([1, 5, 6, 7, 3]), True)
print(isValid([5, 6, 7]), True)
print(isValid([5, 6, 7, 8]), True)
print(isValid([6, 7, 8]), False)
print(isValid([7, 8]), True)
