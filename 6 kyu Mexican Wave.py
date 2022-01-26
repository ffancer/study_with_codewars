def wave(people):
    lst = []

    for i in people:
        if i[0] != ' ':
            i = i[0].upper() + i[1:]
            lst.append(i)

    return lst

print(wave("hello"))
print(wave("codewars"))
print(wave(""))
print(wave("two words"))
print(wave(" gap "))