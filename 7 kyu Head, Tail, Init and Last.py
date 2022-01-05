head = lambda array: array[0]
tail = lambda array: array[1:]
init = lambda array: array[:-1]
last = lambda array: array[-1]


print(head([5, 1]), 5)
print(tail([1]), [])
print(init([1, 5, 7, 9]), [1, 5, 7])
print(last([7, 2]), 2)
