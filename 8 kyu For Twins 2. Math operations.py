# 8 kyu
# For Twins: 2. Math operations


def ice_brick_volume(radius, bottle_length, rim_length):
    return (bottle_length - rim_length) * radius * 2 * radius


print(ice_brick_volume(1, 10, 2), 16)
print(ice_brick_volume(5, 30, 7), 1150)
