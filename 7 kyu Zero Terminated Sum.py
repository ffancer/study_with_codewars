def largest_sum(s):
    if s == '0':
        return 0

    s = s.split('0')
    [s.remove(i) for i in s if i == '']
    lst = []

    for i in s:
        lst.append(sum([int(j) for j in list(i)]))

    return max(lst)


print(largest_sum("72102450111111090"), 11)
print(largest_sum("123004560"), 15)
print(largest_sum("0"), 0)
