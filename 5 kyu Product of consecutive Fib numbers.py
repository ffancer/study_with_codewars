def productFib(prod):
    first, second = 0, 1

    while prod > first * second:
        first, second = second, first + second

    return [first, second, prod == first * second]


print(productFib(4895), [55, 89, True])
print(productFib(5895), [89, 144, False])
