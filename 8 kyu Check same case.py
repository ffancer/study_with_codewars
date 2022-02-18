def same_case(a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
        return 1
    return 0


print(same_case('C', 'B'), 1)
print(same_case('b', 'a'), 1)
print(same_case('d', 'd'), 1)
print(same_case('A', 's'), 0)
print(same_case('c', 'B'), 0)
print(same_case('b', 'Z'), 0)
print(same_case('\t', 'Z'), -1)
print(same_case('H', ':'), -1)
