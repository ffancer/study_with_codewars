# 8 kyu
# Simple Fun #352: Reagent Formula

def isValid(formula):
    if 1 and 2 in formula:
        return False
    if 3 and 4 in formula:
        return False
    if (5 in formula and 6 not in formula) or (6 in formula and 5 not in formula):
        return False

    return True


print(isValid([1, 3, 7]), True)
print(isValid([7, 1, 2, 3]), False)
print(isValid([1, 3, 5, 7]), False)
print(isValid([1, 5, 6, 7, 3]), True)
print(isValid([5, 6, 7]), True)
print(isValid([5, 6, 7, 8]), True)
print(isValid([6, 7, 8]), False)
print(isValid([7, 8]), True)
