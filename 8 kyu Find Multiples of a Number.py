def find_multiples(integer, limit):
    lst = []
    for i in range(1, limit+1):
        if i % integer == 0:
            lst.append(i)

    return lst


print(find_multiples(5, 25), [5, 10, 15, 20, 25])
print(find_multiples(1, 2), [1, 2])