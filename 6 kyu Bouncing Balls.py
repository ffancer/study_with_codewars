import math


def bouncing_ball(h, bounce, window):
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    num_past_window = math.log(window / h, bounce)
    floored_num = int(num_past_window)

    return num_past_window if num_past_window == floored_num else floored_num * 2 + 1


print(bouncing_ball(2, 0.5, 1))  # 1
print(bouncing_ball(3, 0.66, 1.5))  # 3
print(bouncing_ball(30, 0.66, 1.5))  # 15
print(bouncing_ball(30, 0.75, 1.5))  # 21
