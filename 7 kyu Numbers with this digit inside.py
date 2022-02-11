from math import prod


def numbers_with_digit_inside(x, d):
    # lst = [i for i in range(d, x + 1) if str(d) in str(i) and str(i) != '0']
    lst = []

    for i in range(d, x + 1):
        if str(d) in str(i) and str(i) != '0':
            lst.append(i)

    # return [len(lst), sum(lst), prod(lst)]
    cnt, total, prodd = 0, 0, 1
    for i in lst:
        cnt += 1
        total += i
        prodd *= i
    return [cnt, total, prodd]
tests = (
    ((5, 6), [0, 0, 0]),
    ((7, 6), [1, 6, 6]),
    ((11, 1), [3, 22, 110]),
    ((20, 0), [2, 30, 200]),
    ((44, 4), [9, 286, 5955146588160]),
)

for t in tests:
    inp, exp = t
    print(numbers_with_digit_inside(*inp), exp)
