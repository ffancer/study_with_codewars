# 8 kyu
# Thinkful - Number Drills: Pixelart planning

def is_divisible(wall_length, pixel_size):
    return wall_length % pixel_size == 0


print(is_divisible(4050, 27), True)
print(is_divisible(4066, 27), False)
print(is_divisible(10000, 20), True)
print(is_divisible(10005, 20), False)
