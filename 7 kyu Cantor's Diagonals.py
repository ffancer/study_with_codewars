# best practice 1
def cantor(nested_list):
    return [not nested_list[i][i] for i in range(len(nested_list))]


# best practice 2
def cantor(l):
    return [l[i][i] ^ 1 for i in range(len(l))]


# best practice 3
def cantor(nested_list):
    return [-~-arr[index] for index, arr in enumerate(nested_list)]


# best practice 4
def cantor(nested_list):
    l = []
    for i in range(len(nested_list)):
        l.append((nested_list[i][i] + 1) % 2)
    return l


example1 = [[0, 0],
            [1, 1]]

print(cantor(example1), [1, 0])

example2 = [[1, 1],
            [0, 0]]

print(cantor(example2), [0, 1])

example3 = [[0, 1],
            [1, 0]]

print(cantor(example3), [1, 1])

example4 = [[0, 0, 0],
            [1, 1, 1],
            [0, 1, 0]]

print(cantor(example4), [1, 0, 1])

example5 = [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]

print(cantor(example5), [0, 0, 0])
