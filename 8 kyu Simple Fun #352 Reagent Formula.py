# 8 kyu
# Simple Fun #352: Reagent Formula

def isValid(formula):
    return (7 in formula or 8 in formula) and not (1 in formula and 2 in formula) and not (
                3 in formula and 4 in formula) and (
                       (5 in formula and 6 in formula) or (5 not in formula and 6 not in formula))


print(isValid([1, 3, 7]), True)
print(isValid([7, 1, 2, 3]), False)
print(isValid([1, 3, 5, 7]), False)
print(isValid([1, 5, 6, 7, 3]), True)
print(isValid([5, 6, 7]), True)
print(isValid([5, 6, 7, 8]), True)
print(isValid([6, 7, 8]), False)
print(isValid([7, 8]), True)
