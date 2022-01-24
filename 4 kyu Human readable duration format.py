def format_duration(seconds):
    if seconds == 0:
        return 'now'

    year = seconds // 31536000
    seconds = seconds % 31536000
    day = seconds // 86400
    seconds = seconds % 86400
    hour = seconds // 3600
    seconds = seconds % 3600
    minute = seconds // 60
    seconds = seconds % 60
    second = seconds

    lst = []

    if year == 1:
        lst.append("1 year")
    if year >= 2:
        lst.append(str(year) + " years")
    if day == 1:
        lst.append("1 day")
    if day >= 2:
        lst.append(f"{day} days")
    if hour == 1:
        lst.append("1 hour")
    if hour > 1:
        lst.append(f"{hour} hours")
    if minute == 1:
        lst.append("1 minute")
    if minute > 1:
        lst.append(f"{minute} minutes")
    if second == 1:
        lst.append("1 second")
    if seconds > 1:
        lst.append(f"{second} seconds")

    if len(lst) == 1:
        return "".join(lst)
    if len(lst) == 2:
        return " and ".join(lst)
    if len(lst) > 2:
        return ", ".join(lst[:len(lst) - 1]) + " and " + lst[-1]


print(format_duration(1), "1 second")
print(format_duration(62), "1 minute and 2 seconds")
print(format_duration(120), "2 minutes")
print(format_duration(3600), "1 hour")
print(format_duration(3662), "1 hour, 1 minute and 2 seconds")
