def driver(data):
    first = data[2][:6].upper().ljust(5, '9')
    second = data[3].split('-')[2][2]
    return first, second


data = ["John", "James", "Smith", "01-Jan-2000", "M"]
print(driver(data), "SMITH001010JJ9AA")
data = ["Johanna", "", "Gibbs", "13-Dec-1981", "F"]
print(driver(data), "GIBBS862131J99AA")
data = ["Andrew", "Robert", "Lee", "02-September-1981", "M"]
print(driver(data), "LEE99809021AR9AA")
