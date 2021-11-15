def fuel_price(litres, price_per_litre):
    discount = 0
    if 4 > litres >= 2:
        discount = price_per_litre * 0.05
    elif 6 > litres >= 4:
        discount = price_per_litre * 0.1
    elif 8 > litres >= 6:
        discount = price_per_litre * 0.2
    elif 10 >= litres >= 8:
        discount = price_per_litre * 0.25
    return litres * price_per_litre - litres * discount


print(fuel_price(10, 21.5), 212.5)
print(fuel_price(40, 10), 390)
print(fuel_price(15, 5.83), 83.7)
