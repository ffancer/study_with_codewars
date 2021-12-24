def reverse(lst):
    empty_list = list()

    for i in lst:
        empty_list.insert(0, i)

    return empty_list

print(reverse(list([1, 2, 3])), [3, 2, 1])
print(reverse(list([1, None, 14, "two"])), ["two", 14, None, 1])