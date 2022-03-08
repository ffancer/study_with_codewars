# 7 kyu
# Thinking & Testing : Uniq or not Uniq


def testit(a, b):
    srtd_lst = sorted(a + b)
    lst = []

    for i in srtd_lst:
        if srtd_lst.count(i) < 3:
            lst.append(i)

    return lst


print(testit([0], [1]), [0, 1], "")
print(testit([1, 2], [3, 4]), [1, 2, 3, 4], "")
print(testit([1], [2, 3, 4]), [1, 2, 3, 4], "")
print(testit([1, 2, 3], [4]), [1, 2, 3, 4], "")
print(testit([1, 2], [1, 2]), [1, 1, 2, 2], "")
