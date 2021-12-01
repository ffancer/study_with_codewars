# 7 kyu
# Simple Fun #152: Invite More Women?


def invite_more_women(arr):
    return sum(arr) > 0


print(invite_more_women([1, -1, 1]), True)
print(invite_more_women([-1, -1, -1]), False)
print(invite_more_women([1, -1]), False)
print(invite_more_women([1, 1, 1]), True)
