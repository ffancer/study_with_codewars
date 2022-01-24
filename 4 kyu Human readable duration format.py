def format_duration(seconds):
    if seconds == 0:
        return 'now'
    second = seconds % 10
    minute = seconds // 60 % 60
    hour = seconds // 3600
    day = seconds // 86400 % 365
    year = seconds // 31536000

    s = ''
    if year >= 2:
        s += str(year) + " years"
    if day == 1:
        s += "1 day, "
    if day >= 2:
        s += f"{day} days, "
    if 2 > hour > 0:
        s += "1 hour, "
    if hour > 1:
        s += f"{hour} hours, "
    if 2 > minute > 0:
        s += "1 minute, "
    if second == 1:
        s += "1 second"
    if seconds > 2:
        s += f"{second} seconds"
    return s


print(format_duration(1), "1 second")
print(format_duration(62), "1 minute and 2 seconds")
print(format_duration(120), "2 minutes")
print(format_duration(3600), "1 hour")
print(format_duration(3662), "1 hour, 1 minute and 2 seconds")
