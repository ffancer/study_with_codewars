# 7 kyu
# How many are smaller than me?


def smaller(arr):
    i, j, cnt, lst = 0, 1, 0, []

    num = arr[i]

    while arr:
        for k in arr[i:]:
            if num > k:
                cnt += 1
        lst.append(cnt)
        i += 1
        arr = arr[i:]
    return lst

print(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
print(smaller([1, 2, 3]), [0, 0, 0])
print(smaller([1, 2, 0]), [1, 1, 0])
print(smaller([1, 2, 1]), [0, 1, 0])
print(smaller([1, 1, -1, 0, 0]), [3, 3, 0, 0, 0])
print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]), [4, 1, 5, 5, 0, 0, 0, 0, 0])
