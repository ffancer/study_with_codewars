def wrap(height, width, length):
    min_value = min(height, width, length)
    answer = (height * 4 + length * 2 + width * 2) + 20

    if min_value == width:
        answer = (width * 4 + height * 2 + length * 2) + 20
    elif min_value == length:
        answer = (length * 4 + height * 2 + width * 2) + 20
    return answer


print(wrap(17, 32, 11), 162)
print(wrap(13, 13, 13), 124)
print(wrap(1, 3, 1), 32)
