def crap(garden, bags, cap):
    cnt_a, cnt_dog = 0, 0

    for i in garden:
        cnt_a = i.count('@')
        cnt_dog = i.count('D')

    return cnt_a



print(crap([['_', '_', '_', '_'], ['_', '_', '_', '@'], ['_', '_', '@', '_']], 2, 2), "Clean")
print(crap([['_', '_', '_', '_'], ['_', '_', '_', '@'], ['_', '_', '@', '_']], 1, 1), "Cr@p")
print(crap([['_', '_'], ['_', '@'], ['D', '_']], 2, 2), "Dog!!")
print(crap([['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_']], 2, 2), "Clean")
print(crap([['@', '@'], ['@', '@'], ['@', '@']], 3, 2), "Clean")
