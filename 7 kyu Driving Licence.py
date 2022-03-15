def driver(data):
    month = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': "06",
        'Jul': "07",
        'Aug': "08",
        'September': "09",
        'Oct': "10",
        'Nov': "11",
        'Dec': "12"
    }

    first = data[2][:6].upper().ljust(5, '9')
    second = data[3].split('-')[2][2]
    third = ''
    a = data[3].split('-')
    if data[-1] == 'F':
        third += str(int(month.get(a[1])[0]) + 5) + month.get(a[1])[1]
    return third

data = ["John", "James", "Smith", "01-Jan-2000", "M"]
print(driver(data), "SMITH001010JJ9AA")
data = ["Johanna", "", "Gibbs", "13-Dec-1981", "F"]
print(driver(data), "GIBBS862131J99AA") # 62
data = ["Andrew", "Robert", "Lee", "02-September-1981", "M"]
print(driver(data), "LEE99809021AR9AA")
