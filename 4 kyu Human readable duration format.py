def format_duration(seconds):
    if seconds == 0:
        return 'now'
    second = seconds % 10
    minute = seconds // 60 % 60
    hour = seconds // 3600

    s = ''

    if 2 > hour > 0:
        s += "1 hour, "
    if hour > 1:
        s += f"{hour} hours, "

    return s


print(format_duration(1), "1 second")
print(format_duration(62), "1 minute and 2 seconds")
print(format_duration(120), "2 minutes")
print(format_duration(3600), "1 hour")
print(format_duration(3662), "1 hour, 1 minute and 2 seconds")
