import itertools

def next_bigger(n):
    answer = -1
    i, j = 0, 1

    # lst = list(map(int, str(n)))
    set_of_nums = set([int(''.join(i)) for i in itertools.permutations(str(n), len(str(n)))])

    return set_of_nums


print(next_bigger(12), 21)
print(next_bigger(1228881758))
# print(next_bigger(513),531)
# print(next_bigger(2017),2071)
# print(next_bigger(414),441)
# print(next_bigger(144),414)
