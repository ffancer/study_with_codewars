def is_narcissistic(i):
    return sum(int(j) ** len(str(i)) for j in str(i)) == i


print(is_narcissistic(153), True)
print(is_narcissistic(201), False)
print(is_narcissistic(259), False)
print(is_narcissistic(371), True)
print(is_narcissistic(407), True)
print(is_narcissistic(595), False)
print(is_narcissistic(825), False)
print(is_narcissistic(1634), True)
