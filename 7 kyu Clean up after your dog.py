def crap(garden, bags, cap):
    cnt_a, cnt_dog = 0, 0

    for i in garden:
        for j in i:
            if j == '@':
                cnt_a += 1
            if j == 'D':
                cnt_dog += 1

    if cnt_dog >= 1:
        return 'Dog!!'
    if cnt_a > cap:
        return 'Cr@p'
    if cnt_a <= cap:
        return 'Clean'



print(crap([['_', '_', '_', '_'], ['_', '_', '_', '@'], ['_', '_', '@', '_']], 2, 2), "Clean")
print(crap([['_', '_', '_', '_'], ['_', '_', '_', '@'], ['_', '_', '@', '_']], 1, 1), "Cr@p")
print(crap([['_', '_'], ['_', '@'], ['D', '_']], 2, 2), "Dog!!")
print(crap([['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_']], 2, 2), "Clean")
print(crap([['@', '@'], ['@', '@'], ['@', '@']], 3, 2), "Clean")
