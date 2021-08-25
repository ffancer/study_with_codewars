def count_sheep(n):
    # first
    # s = ''
    #
    # for i in range(1, n+1):
    #     s += f'{i} sheep...'
    #
    # return s

    # second
    return ''.join([f'{i} sheep...' for i in range(1, n+1)])





print(count_sheep(1))
print(count_sheep(2))
print(count_sheep(3))