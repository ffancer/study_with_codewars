def db_sort(arr):
    lst_nums, lst_letters = [], []

    for i in arr:
        if type(i) == int:
            lst_nums.append(i)
        else:
            lst_letters.append(i)

    return sorted(lst_nums) + sorted(lst_letters)


print(db_sort([6, 2, 3, 4, 5]), [2, 3, 4, 5, 6])
print(db_sort([14, 32, 3, 5, 5]), [3, 5, 5, 14, 32])
print(db_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
print(db_sort(["Banana", "Orange", "Apple", "Mango", 0, 2, 2]),
      [0, 2, 2, "Apple", "Banana", "Mango", "Orange"])
print(db_sort(["C", "W", "W", "W", 1, 2, 0]), [0, 1, 2, "C", "W", "W", "W"])
print(db_sort(['come', 'on', 110, '2500', 10, '!', 7, 15, 5, 6, 6]),
      [5, 6, 6, 7, 10, 15, 110, "!", "2500", "come", "on"])
print(db_sort(["Apple", 46, "287", 574, "Peach", "3", "69", 78, "Grape", "423"]),
      [46, 78, 574, '287', '3', '423', '69', 'Apple', 'Grape', 'Peach'])
