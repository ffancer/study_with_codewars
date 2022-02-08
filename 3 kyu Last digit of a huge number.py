def last_digit(lst):
    num = 1

    for i in lst[::-1]:
        num = i ** (num if num < 4 else num % 4 + 4)
    return num % 10


print(last_digit([]))
print(last_digit([0, 0]))
print(last_digit([0, 0, 0]))
print(last_digit([1, 2]))
print(last_digit([3, 4, 5]))
print(last_digit([4, 3, 6]))
print(last_digit([7, 6, 21]))
print(last_digit([12, 30, 21]))
print(last_digit([2, 2, 2, 0]))
print(last_digit([937640, 767456, 981242]))
print(last_digit([123232, 694022, 140249]))
print(last_digit([499942, 898102, 846073]))