# best practice 1:
WEEK = ' Sunday Monday Tuesday Wednesday Thursday Friday Saturday'.split(" ")


def whatday(n):
    return WEEK[n] if 0 < n < 8 else 'Wrong, please enter a number between 1 and 7'


# best practice 2:
WEEKDAY = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday'}
ERROR = 'Wrong, please enter a number between 1 and 7'


def whatday(n):
    return WEEKDAY.get(n, ERROR)


# best practice 3:
def whatday(num):
    switcher = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    return switcher.get(num, 'Wrong, please enter a number between 1 and 7')


print(whatday(1), 'Sunday')
print(whatday(2), 'Monday')
print(whatday(3), 'Tuesday')
print(whatday(8), 'Wrong, please enter a number between 1 and 7')
print(whatday(20), 'Wrong, please enter a number between 1 and 7')
