# Заполнить массив нулями, кроме первого и последнего элементов, которые должны быть равны единице.
# Fill the array with zeros, except for the first and last elements, which must be equal to one.


def fill_list(n):
    if n < 3:
        return [1]
    lst = [str(i).replace(str(i), '0') for i in range(n)]
    lst = [int(i) for i in lst]
    return [1] + lst[1:-1] + [1]


print(fill_list(6))
print(fill_list(10))
print(fill_list(1))
print(fill_list(3))
print(fill_list(0))