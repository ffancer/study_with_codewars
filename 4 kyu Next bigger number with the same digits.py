import itertools


def next_bigger(n):
    # n = list(str(n))
    # n = [int(i) for i in n]
    # first_digit = str(n[0])
    # n = n[1::]
    # n.sort(reverse=True)
    # return int(first_digit + ''.join([str(i) for i in n]))
    n = list(str(n))
    n = [int(i) for i in n]
    combinations = list(itertools.permutations(n))
    print(combinations)
    # return n

print(next_bigger(12),21)
print(next_bigger(513),531)
print(next_bigger(2017),2071)
print(next_bigger(414),441)
print(next_bigger(144),414)