# Заполнить массив нулями, кроме первого и последнего элементов, которые должны быть равны единице.
# Fill the array with zeros, except for the first and last elements, which must be equal to one.

n = 5
lst = [str(i).replace(str(i), '0') for i in range(n)]
lst = [int(i) for i in lst]
print([1] + lst[1:-1] + [1])