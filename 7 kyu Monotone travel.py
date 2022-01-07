def is_monotone(heights):
    for i,j in zip(heights, heights[1:]):
        print(i, j)


print(is_monotone(list(range(1, 11))), 'Should work on increasing lists')
print(is_monotone([5, 5, 5, 5, 5, 5, 5]), 'Should work on constant lists')
print(is_monotone([]), 'Should work on empty list')
print(is_monotone([1]), 'Should work on size 1 list')

print(not is_monotone(list(range(5, 0, -1))), 'Should return false on a decreasing list')
print(not is_monotone(list(range(5, -40, -1))), 'Should return false on a decreasing list')
