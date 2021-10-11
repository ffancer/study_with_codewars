# 8 kyu
# Is your period late?
def period_is_late(last, today, cycle_length):
    return (today - last).days > cycle_length


print(period_is_late(2016, 6, 13))
print(period_is_late(2016, 6, 13))
print(period_is_late(2016, 6, 13))
print(period_is_late(2016, 6, 13))
print(period_is_late(2016, 7, 12))
print(period_is_late(2016, 7, 12))
print(period_is_late(2016, 7, 1))
print(period_is_late(2016, 6, 1))
print(period_is_late(2016, 1, 1))
print(period_is_late(2016, 1, 1))
