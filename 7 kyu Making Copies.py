def copy_list(l):
    return l.copy()


t = [1, 2, 3, 4]
t_copy = copy_list(t)
print(t, t_copy)  # copy should be the same

t[1] += 5
print(t, t_copy)  # copy should NOT be the same anymore
