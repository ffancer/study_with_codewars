def check_three_and_two(array):
    pass


print(check_three_and_two(["a", "a", "a", "b", "b"]), True, str(["a", "a", "a", "b", "b"]))
print(check_three_and_two(["a", "c", "a", "c", "b"]), False, str(["a", "c", "a", "c", "b"]))
print(check_three_and_two(["a", "a", "a", "a", "a"]), False, str(["a", "a", "a", "a", "a"]))