def bits_battle(numbers):
    s_odd, s_even = '', ''

    for i in numbers:
        if i % 2 != 0:
            s_odd += bin(i)[2:]
        else:
            s_even += bin(i)[2:]
    return s_odd.count('1'), s_even.count('0')


print(bits_battle([5, 3, 14]), 'odds win')
print(bits_battle([3, 8, 22, 15, 78]), 'evens win')
print(bits_battle([]), 'tie')
print(bits_battle([1, 13, 16]), 'tie')
