def remove_every_other(my_list):
    # first
    lst = []

    for i in range(len(my_list)):
        if i % 2 == 0:
            lst.append(my_list[i])

    return lst




print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(remove_every_other([[1, 2]]))
print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))