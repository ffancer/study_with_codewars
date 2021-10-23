def cantor(nested_list):
    lst = []
    i = 0
    j = 0

    while j < len(nested_list):
        if nested_list[i][j] == 0:
            lst.append(1)
        else:
            lst.append(0)
        i += 1
        j += 1

    return lst

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
