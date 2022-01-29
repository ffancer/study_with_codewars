# 6 kyu
# Are they the "same"?


def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(a1, a2), True)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(a1, a2), False)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(a1, a2), False)
