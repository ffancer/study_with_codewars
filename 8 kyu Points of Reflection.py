def symmetric_point(p, q):
    return [q[0] * 2 - p[0], q[1] * 2 - p[1]]


print(symmetric_point([0, 0], [1, 1]), [2, 2])
print(symmetric_point([2, 6], [-2, -6]), [-6, -18])
print(symmetric_point([10, -10], [-10, 10]), [-30, 30])
print(symmetric_point([1, -35], [-12, 1]), [-25, 37])
print(symmetric_point([1000, 15], [-7, -214]), [-1014, -443])
print(symmetric_point([0, 0], [0, 0]), [0, 0])
print(symmetric_point([0, 1], [2, 3]), [4, 5])  # my test
