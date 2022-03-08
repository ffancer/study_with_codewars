# 7 kyu
# Thinking & Testing : Uniq or not Uniq


def testit(a, b):
    return sorted(a + b)


print(testit([0], [1]), [0, 1], "")
print(testit([1, 2], [3, 4]), [1, 2, 3, 4], "")
print(testit([1], [2, 3, 4]), [1, 2, 3, 4], "")
print(testit([1, 2, 3], [4]), [1, 2, 3, 4], "")
print(testit([1, 2], [1, 2]), [1, 1, 2, 2], "")
