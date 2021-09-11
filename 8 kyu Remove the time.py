def shorten_to_date(long_date):
    s = ''

    for i in range(len(long_date)):
        if long_date[i] == ',':
            s += long_date[:i]

    return s



print(shorten_to_date("Monday February 2, 8pm"), "Monday February 2")
print(shorten_to_date("Tuesday May 29, 8pm"), "Tuesday May 29")
print(shorten_to_date("Wed September 1, 3am"), "Wed September 1")
print(shorten_to_date("Friday May 2, 9am"), "Friday May 2")
print(shorten_to_date("Tuesday January 29, 10pm"), "Tuesday January 29")