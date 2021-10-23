def cantor(nested_list):
    return


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
