def excluding_vat_price(price):
    return -1 if price is None or price <= 0 else round(price / 1.15, 2)


print(excluding_vat_price(230.00), 200.00)
print(excluding_vat_price(123), 106.96)
