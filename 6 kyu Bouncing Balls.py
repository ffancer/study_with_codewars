from math import log


def bouncing_ball(h, bounce, window):
    answer = -1

    while h > window:
        answer += 2
        h *= bounce
    return answer

print(bouncing_ball(2, 0.5, 1))  # 1
print(bouncing_ball(3, 0.66, 1.5))  # 3
print(bouncing_ball(30, 0.66, 1.5))  # 15
print(bouncing_ball(30, 0.75, 1.5))  # 21
