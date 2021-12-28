def bits_battle(numbers):
    lst_odd, lst_even = [], []

    for i in numbers:
        if i % 2 != 0:
            lst_odd.append(i)
            lst_odd.append(bin(i)[2:])
        else:
            lst_even.append(i)
            lst_even.append(bin(i)[2:])

    return lst_odd, lst_even


print(bits_battle([5, 3, 14]), 'odds win')
print(bits_battle([3, 8, 22, 15, 78]), 'evens win')
print(bits_battle([]), 'tie')
print(bits_battle([1, 13, 16]), 'tie')
