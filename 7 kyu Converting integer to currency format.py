def to_currency(price):
    i = -3
    lst = []
    while i < 0:
        lst.append(str(price)[-3:])
        price = str(price)[:-3]

    return lst
    # return list(str(price)).pop(3)


print(to_currency(123456), "123,456")
print(to_currency(1234), "1,234")
print(to_currency(123), "123")
print(to_currency(123456789012), "123,456,789,012")
