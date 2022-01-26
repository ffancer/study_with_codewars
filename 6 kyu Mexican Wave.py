def wave(people):
    lst = []

    for i in range(len(people)):
        if people[i] != ' ':
            lst.append(people[:i] + people[i].upper() + people[i+1:])

    return lst

print(wave("hello"))
print(wave("codewars"))
print(wave(""))
print(wave("two words"))
print(wave(" gap "))