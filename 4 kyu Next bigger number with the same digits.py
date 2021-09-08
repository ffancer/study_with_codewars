import math


def next_bigger(number):
    lst = []
    j = 0

    while number != 0:
        lst.append(number % 10)
        number = math.trunc(number/10)
        j += 1

    lst = lst[::-1]

    for i in range(j - 1, -1, -1):

        for k in range(i - 1, -1, -1):
            if lst[i] > lst[k]:
                lst[i], lst[k] = lst[k], lst[i]
                lst = lst[:k + 1] + sorted(lst[k+1:])
                cnt = 1
                result = 0

                for item in range(j):
                    result += lst[item] * (10 ** (j - cnt))
                    cnt += 1

                return result

print(next_bigger(12), 21)
print(next_bigger(1228881758))
print(next_bigger(513),531)
print(next_bigger(2017),2071)
print(next_bigger(414),441)
print(next_bigger(144),414)
