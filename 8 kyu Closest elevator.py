def elevator(left, right, call):
    a = call - left
    b = call - right

    return 'left' if a - b == 0 else 'right'

print(elevator(0, 1, 0), "left")
print(elevator(0, 1, 1), "right")
print(elevator(0, 1, 2), "right")
print(elevator(0, 0, 0), "right")
print(elevator(0, 2, 1), "right")