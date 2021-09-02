def super_size(n):
    # first
    # n = list(str(n))
    # n = sorted([int(i) for i in n], reverse=True)
    # return int(''.join([str(i) for i in n]))

    #second
    return ''.join(sorted(str(n), reverse=True))

print(super_size(69), 96)
print(super_size(513), 531)
print(super_size(2017), 7210)
print(super_size(414), 441)
print(super_size(608719), 987610)
print(super_size(123456789), 987654321)
print(super_size(700000000001), 710000000000)
print(super_size(666666), 666666)
print(super_size(2), 2)
print(super_size(0), 0)