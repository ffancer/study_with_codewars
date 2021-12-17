from datetime import date


def unlucky_days(year):
    return sum(date(year, m, 13).strftime('%A') == 'Friday' for m in range(1, 13))


print(unlucky_days(1634), 2)
print(unlucky_days(2873), 2)
