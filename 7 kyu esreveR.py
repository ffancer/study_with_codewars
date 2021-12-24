def reverse(lst):
    empty_list = list()
    i = len(lst) - 1

    while i != -1:
        empty_list.append(lst[i])
        i -= 1

    return empty_list

print(reverse(list([1, 2, 3])), [3, 2, 1])
print(reverse(list([1, None, 14, "two"])), ["two", 14, None, 1])