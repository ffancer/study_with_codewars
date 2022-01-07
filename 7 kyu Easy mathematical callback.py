def process_array(arr, callback):
    return [callback(i) for i in arr]




my_array = [4, 8, 2, 7, 5]
func = lambda val: val * 2
my_array = process_array(my_array, func)
print(my_array, [8, 16, 4, 14, 10], 'The result array is wrong.')

my_array = [7, 8, 9, 1, 2]
func = lambda val: val + 5
my_array = process_array(my_array, func)
print(my_array, [12, 13, 14, 6, 7], 'The result array is wrong.')

my_array = [-1, 1, 2, 3, 4, 5]
func = lambda val: val ** 3
my_array = process_array(my_array, func)
print(my_array, [-1, 1, 8, 27, 64, 125], 'The result array is wrong.')

my_array = []
func = lambda val: val + 1
my_array = process_array(my_array, func)
print(my_array, [], 'The result array is wrong.')
