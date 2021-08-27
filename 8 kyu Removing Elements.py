def remove_every_other(my_list):
    # Your code here!
    pass


print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),
                   ['Hello', 'Hello Again'])
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                   [1, 3, 5, 7, 9])
print(remove_every_other([[1, 2]]), [[1, 2]])
print(remove_every_other([['Goodbye'], {'Great': 'Job'}]),
                   [['Goodbye']])