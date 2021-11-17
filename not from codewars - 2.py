# Заполнить массив нулями и единицами, при этом данные значения чередуются, начиная с нуля.
# Fill the array with zeros and ones, with these values ​​alternating starting from zero.


def fill_list(n):
    return [1 if i % 2 != 0 else 0 for i in range(n)]

print(fill_list(0))
print(fill_list(2))
print(fill_list(10))
print(fill_list(5))