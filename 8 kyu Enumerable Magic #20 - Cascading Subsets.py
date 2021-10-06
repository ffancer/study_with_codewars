def each_cons(lst, n):
    return [lst[i:i+n] for i in list(range(len(lst) - n + 1))]


lst = [3, 5, 8, 13]
print(each_cons(lst, 2), [[3, 5], [5, 8], [8, 13]])
