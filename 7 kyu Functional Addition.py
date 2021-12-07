def add(n):
    def add_temp(x):
        return n + x

    return add_temp


add_one = add(1)
print(add_one(3), 4)
add_three = add(3)
print(add_three(3), 6)
