def to_currency(price):
    lst = []

    while price:
        lst.append(str(price)[-3:])
        price = str(price)[:-3]

    return ','.join(reversed(lst))



print(to_currency(123456), "123,456")
print(to_currency(1234), "1,234")
print(to_currency(123), "123")
print(to_currency(123456789012), "123,456,789,012")
