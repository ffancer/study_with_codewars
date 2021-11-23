def find_longest(arr):
    arr = [str(i) for i in arr]

    longest_num = ''

    for i in arr:
        if len(i) > len(longest_num):
            longest_num = i

    return int(longest_num)


print(find_longest([1, 10, 100]), 100)
print(find_longest([9000, 8, 800]), 9000)
print(find_longest([8, 900, 500]), 900)
print(find_longest([3, 40000, 100]), 40000)
print(find_longest([1, 200, 100000]), 100000)
