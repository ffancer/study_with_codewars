def solve(s):
    cnt = 0
    lst = []

    for i in s:
        if i in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
        else:
            lst.append(cnt)
            cnt = 0

    return max(lst)


print(solve("codewarriors"), 2)
print(solve("suoidea"), 3)
print(solve("ultrarevolutionariees"), 3)
print(solve("strengthlessnesses"), 1)
print(solve("cuboideonavicuare"), 2)
print(solve("chrononhotonthuooaos"), 5)
print(solve("iiihoovaeaaaoougjyaw"), 8)
