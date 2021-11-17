# Заполнить массив последовательными нечетными числами, начиная с единицы.
# Fill the array with consecutive odd numbers, starting at one.

def fill_list(n):
    lst = []
    i = 1

    while len(lst) < n:
        lst.append(i)
        i += 2

    return lst

print(fill_list(0))
print(fill_list(1))
print(fill_list(5))
print(fill_list(11))
print(fill_list(15))