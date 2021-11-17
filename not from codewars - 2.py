# Заполнить массив нулями и единицами, при этом данные значения чередуются, начиная с нуля.
# Fill the array with zeros and ones, with these values ​​alternating starting from zero.


def fill_list(n):
    lst = []

    for i in range(n):
        if i % 2 != 0:
            lst.append(1)
        else:
            lst.append(0)

    return lst


print(fill_list(0))
print(fill_list(2))
print(fill_list(10))
print(fill_list(5))