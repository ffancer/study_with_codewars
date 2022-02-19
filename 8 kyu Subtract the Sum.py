from math import prod



def subtract_sum(number):
    number = list(str(number))
    number = [int(i) for i in number]
    return prod(number)


print(subtract_sum(10), "apple")
