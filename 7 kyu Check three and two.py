def check_three_and_two(array):
    cnt_a = array.count('a')
    cnt_b = array.count('b')
    cnt_c = array.count('c')

    if (cnt_a == 3 and cnt_b == 2) or (cnt_a == 3 and cnt_c == 2):
        return True
    if (cnt_b == 3 and cnt_a == 2) or (cnt_b == 3 and cnt_c == 2):
        return True
    if (cnt_c == 3 and cnt_b == 2) or (cnt_c == 3 and cnt_a == 2):
        return True
    return False


print(check_three_and_two(["a", "a", "a", "b", "b"]), True, str(["a", "a", "a", "b", "b"]))
print(check_three_and_two(["a", "c", "a", "c", "b"]), False, str(["a", "c", "a", "c", "b"]))
print(check_three_and_two(["a", "a", "a", "a", "a"]), False, str(["a", "a", "a", "a", "a"]))
