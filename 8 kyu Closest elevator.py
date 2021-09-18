def elevator(left, right, call):
    return 'left' if abs(call - left) < abs(call - right) else 'right'

print(elevator(0, 1, 0), "left")
print(elevator(0, 1, 1), "right")
print(elevator(0, 1, 2), "right")
print(elevator(0, 0, 0), "right")
print(elevator(0, 2, 1), "right")