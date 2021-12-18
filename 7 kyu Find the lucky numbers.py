def filter_lucky(lst):
    return [i for i in lst if '7' in str(i)]



print(filter_lucky([1,2,3,4,5,6,7,68,69,70,15,17]))
print(filter_lucky([7]))
print(filter_lucky([1, 2, 3]))
print(filter_lucky([77, 8]))
print(filter_lucky([71]))
print(filter_lucky([71, 9907, 69]))
