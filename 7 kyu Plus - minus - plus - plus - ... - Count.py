def catch_sign_change(lst):
    cnt = 0

    for i in range(1, len(lst)):
        if lst[i] < 0 and lst[i-1] >= 0:
            cnt += 1
        if lst[i] >= 0 and lst[i-1] < 0:
            cnt += 1

    return cnt


print(catch_sign_change([1, 3, 4, 5]), 0)
print(catch_sign_change([1, -3, -4, 0, 5]), 2)
print(catch_sign_change([]), 0)
print(catch_sign_change([-47, 84, -30, -11, -5, 74, 77]), 3)
