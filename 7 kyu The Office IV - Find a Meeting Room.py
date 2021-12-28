def meeting(rooms):
    for i,j in enumerate(rooms):
        if j == 'O':
            return i
    return 'None available!'


print(meeting(['X', 'O', 'X']), 1)
print(meeting(['O', 'X', 'X', 'X', 'X']), 0)
print(meeting(['X', 'X', 'O', 'X', 'X']), 2)
print(meeting(['X']), 'None available!')
