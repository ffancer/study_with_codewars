# 7 kyu
# Simple Fun #74: Growing Plant


def growing_plant(upSpeed, downSpeed, desiredHeight):
    if upSpeed == desiredHeight:
        return 1

    cnt = 1
    up = upSpeed

    while upSpeed <= desiredHeight:
        cnt += 1
        upSpeed += up - downSpeed
        if upSpeed >= desiredHeight:
            break

    return cnt


print(growing_plant(100, 10, 910), 10)
print(growing_plant(10, 9, 4), 1)
print(growing_plant(5, 2, 0), 1)
print(growing_plant(5, 2, 5), 1)
print(growing_plant(5, 2, 6), 2)
