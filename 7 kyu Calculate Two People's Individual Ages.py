def get_ages(sum_, difference):
    if sum_ < 0 or difference < 0:
        return None

    old = sum_ / 2 + difference / 2
    young = sum_ / 2 - difference / 2

    if old < 0 or young < 0:
        return None

    return old, young


print(get_ages(24, 4), (14, 10))
print(get_ages(63, -14), None)
