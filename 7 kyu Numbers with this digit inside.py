def numbers_with_digit_inside(x, d):
    pass


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
