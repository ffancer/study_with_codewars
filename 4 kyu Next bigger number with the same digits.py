import itertools


def next_bigger(n):
    m = n
    lst = []
    n = list(str(n))
    n = [int(i) for i in n]
    combinations = list(itertools.permutations(n))

    for i in combinations:
        lst.append(int(''.join(map(str, i))))

    lst = sorted(lst)

    for i in range(len(lst)):
        if lst[i] == m:
            return lst[i+1]


print(next_bigger(12),21)
print(next_bigger(513),531)
print(next_bigger(2017),2071)
print(next_bigger(414),441)
print(next_bigger(144),414)