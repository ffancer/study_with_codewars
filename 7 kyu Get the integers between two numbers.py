def function(start_num, end_num):
    lst = []

    for i in range(start_num+1, end_num):
        lst.append(i)

    return lst


print(function(2, 9), [3, 4, 5, 6, 7, 8])
print(function(6, 8), [7])
print(function(2, 9), [3, 4, 5, 6, 7, 8])
