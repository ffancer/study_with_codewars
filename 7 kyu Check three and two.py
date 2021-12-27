def check_three_and_two(array):
    cnt = 0
    if array.count('a') in [3, 2]:
        cnt += 1
    if array.count('b') in [3, 2]:
        cnt += 1
    if array.count('c') in [3, 2]:
        cnt += 1

    return cnt >= 2


print(check_three_and_two(["a", "a", "a", "b", "b"]), True, str(["a", "a", "a", "b", "b"]))
print(check_three_and_two(["a", "c", "a", "c", "b"]), False, str(["a", "c", "a", "c", "b"]))
print(check_three_and_two(["a", "a", "a", "a", "a"]), False, str(["a", "a", "a", "a", "a"]))
