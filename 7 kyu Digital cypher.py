def encode(message, key):
    lst = []

    for i in message:
        lst.append((ord(i)-96)% 26)

    return lst


print(encode("abcde", 1939), [1,2,3,4,5])
print(encode("scout", 1939), [20, 12, 18, 30, 21])
print(encode("masterpiece", 1939), [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8])
