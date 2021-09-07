def find_multiples(integer, limit):
    #second
    return [i for i in range(1, limit+1) if i % integer == 0]


print(find_multiples(5, 25), [5, 10, 15, 20, 25])
print(find_multiples(1, 2), [1, 2])
