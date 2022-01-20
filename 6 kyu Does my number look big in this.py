def narcissistic(value):
    num = 0

    for i in str(value):
        num += int(i) ** int(len(str(value)))

    return num == value


print(narcissistic(153), True)
print(narcissistic(1652), False)
print(narcissistic(7), True, '7 is narcissistic')
print(narcissistic(371), True, '371 is narcissistic')
print(narcissistic(122), False, '122 is not narcissistic')
print(narcissistic(4887), False, '4887 is not narcissistic')
