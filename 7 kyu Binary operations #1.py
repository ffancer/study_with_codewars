def flip_bit(value, bit_index):
    return value ^ (1 << (bit_index - 1))


print(flip_bit(15, 4), 7)
print(flip_bit(15, 5), 31)
print(flip_bit(0, 16), 1 << 15)
print(flip_bit((1 << 31) - 1, 31), (1 << 30) - 1)
print(flip_bit(127, 8), 0xFF)
