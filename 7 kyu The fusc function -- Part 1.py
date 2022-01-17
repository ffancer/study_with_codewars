def fusc(n):
    assert type(n) == int and n >= 0
    # Your code here


print(fusc(0), 0)
print(fusc(1), 1)
print([fusc(i) for i in range(21)], [0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3])
print(fusc(85), 21)
