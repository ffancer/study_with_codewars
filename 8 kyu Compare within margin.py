def close_compare(a, b, margin=0):
    if abs(a-b) <= margin:
        return 0
    elif a < b:
        return -1
    return 1


print(close_compare(4, 5), -1)
print(close_compare(5, 5), 0)
print(close_compare(6, 5), 1)
print('*' * 60)
print(close_compare(2, 5, 3), 0)
print(close_compare(5, 5, 3), 0)
print(close_compare(8, 5, 3), 0)
print(close_compare(8.1, 5, 3), 1)
print(close_compare(1.99, 5, 3), -1)
