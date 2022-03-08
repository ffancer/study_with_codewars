# 7 kyu
# Thinking & Testing : Uniq or not Uniq


def testit(a, b):
    a.extend(b)  # extend???
    return a


print(testit([0], [1]), [0, 1], "")
print(testit([1, 2], [3, 4]), [1, 2, 3, 4], "")
print(testit([1], [2, 3, 4]), [1, 2, 3, 4], "")
print(testit([1, 2, 3], [4]), [1, 2, 3, 4], "")
print(testit([1, 2], [1, 2]), [1, 1, 2, 2], "")
