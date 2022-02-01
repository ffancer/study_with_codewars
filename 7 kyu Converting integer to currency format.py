def to_currency(price):
    i = -3
    cnt = 3
    lst = []
    x = -1
    while i < 0:
        lst.append(str(price)[-i:x])
        i -= 3
        x -= 3
    return lst
    # return str(price)[-6:]


print(to_currency(123456), "123,456")
print(to_currency(1234), "1,234")
print(to_currency(123), "123")
print(to_currency(123456789012), "123,456,789,012")
