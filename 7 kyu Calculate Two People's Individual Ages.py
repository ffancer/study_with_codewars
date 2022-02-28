def get_ages(sum_, difference):
    old = sum_ // 2 + difference // 2
    young = sum_ // 2 - difference // 2
    return old, young

print(get_ages(24, 4), (14, 10))
print(get_ages(63, -14), None)
