from math import ceil


def balanced_num(number):
    number = str(number)
    number_len = len(number)
    lst = [int(i) for i in str(number)]
    number_len_ceil = ceil(number_len / 2)

    if number_len % 2 == 0:
        if sum(lst[:int(number_len_ceil - 1)]) == sum(lst[int(number_len_ceil + 1):]):
            return 'Balanced'
        else:
            return 'Not Balanced'
    else:
        if sum(lst[:int(number_len_ceil - 1)]) == sum(lst[int(number_len_ceil):]):
            return "Balanced"
        return 'Not Balanced'



print(balanced_num(7), "Balanced")
print(balanced_num(959), "Balanced")
print(balanced_num(13), "Balanced")
print(balanced_num(432), "Not Balanced")
print(balanced_num(424), "Balanced")

print(balanced_num(1024), "Not Balanced")
print(balanced_num(66545), "Not Balanced")
print(balanced_num(295591), "Not Balanced")
print(balanced_num(1230987), "Not Balanced")
print(balanced_num(56239814), "Balanced")
