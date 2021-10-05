def whatday(num):
    try:
        days = {
            1: 'Sunday',
            2: 'Monday',
            3: 'Tuesday',
            4: 'Wednesday',
            5: 'Thursday',
            6: 'Friday',
            7: 'Saturday',
        }

        return days[num]
    except:
        return 'Wrong, please enter a number between 1 and 7'



print(whatday(1), 'Sunday')
print(whatday(2), 'Monday')
print(whatday(3), 'Tuesday')
print(whatday(8), 'Wrong, please enter a number between 1 and 7')
print(whatday(20), 'Wrong, please enter a number between 1 and 7')
