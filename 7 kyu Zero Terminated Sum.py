def largest_sum(s):
    return max(sum(map(int,x)) for x in s.split('0'))


print(largest_sum("72102450111111090"), 11)
print(largest_sum("123004560"), 15)
print(largest_sum("0"), 0)
