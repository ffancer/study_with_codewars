def name_value(my_list):
    return [sum(ord(ch) - ord('a') + 1 for ch in elem.replace(' ', '')) * i for i, elem in enumerate(my_list, 1)]




print(name_value(["codewars", "abc", "xyz"]), [88, 12, 225])
print(name_value(["abc abc", "abc abc", "abc", "abc"]), [12, 24, 18, 24])