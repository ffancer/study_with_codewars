from math import prod


def multi(l_st):
    return prod(i for i in l_st)


def add(l_st):
    return sum(l_st)


def reverse(string):
    return string.reverse()


print(multi([8, 2, 5]), 80)
print(add([1, 15, 3]), 19)
print(add([7, 8, 6, 5, 4, 9]), 39)
print(reverse("Hello World"), "dlroW olleH")
