def most_frequent_item_count(collection):
    lst = []

    for i in collection:
        lst.append(collection.count(i))

    return 0 if len(lst) < 1 else max(lst)


print(most_frequent_item_count([3, -1, -1]), 2, "didn't work for [3, -1, -1]")
print(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]), 5,
      "didn't work for [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]")
print(most_frequent_item_count([]), 0, "didn't work for []")
print(most_frequent_item_count([9]), 1, "didn't work for [9]")
