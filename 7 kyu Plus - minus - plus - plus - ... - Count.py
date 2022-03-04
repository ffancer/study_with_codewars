def catch_sign_change(lst):
    # lst = [str(i) for i in lst]
    cnt = 0
    x = lst[0]
    if x < 0:
        for i in lst[1:]:
            if




print(catch_sign_change([1, 3, 4, 5]), 0)
print(catch_sign_change([1, -3, -4, 0, 5]), 2)
print(catch_sign_change([]), 0)
print(catch_sign_change([-47, 84, -30, -11, -5, 74, 77]), 3)
