import itertools


def next_bigger(n):
    lst = []
    n = list(str(n))
    n = [int(i) for i in n]
    combinations = list(itertools.permutations(n))
    # print(combinations)
    for i in combinations:
        lst.append(''.join(map(str, i)))

    return lst

print(next_bigger(12),21)
print(next_bigger(513),531)
print(next_bigger(2017),2071)
print(next_bigger(414),441)
print(next_bigger(144),414)