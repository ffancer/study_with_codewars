# 7 kyu
# Simple Fun #3: Late Ride


def late_ride(n):
    # hour = (n - n % 60) / 60
    # minute = n % 60
    # return hour, minute

    hour = n / 60
    minute = n % 60
    return hour / 10 + hour % 10 + minute / 10 + minute % 10


print(late_ride(240), 4)
print(late_ride(808), 14)
print(late_ride(1439), 19)
print(late_ride(0), 0)
print(late_ride(23), 5)
print(late_ride(8), 8)
