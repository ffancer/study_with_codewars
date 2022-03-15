months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def driver(data):
    first, middle, surname, birth, sex = data
    day, month, year = birth.split("-")

    return "%s%s%02d%s%s%s%s9AA" % ((surname.upper() + "9999")[:5],
                                    year[-2], months.index(month[:3]) + (51 if sex == "F" else 1),
                                    day, year[-1], first[0], (middle + "9")[0])


data = ["John", "James", "Smith", "01-Jan-2000", "M"]
print(driver(data), "SMITH001010JJ9AA")
data = ["Johanna", "", "Gibbs", "13-Dec-1981", "F"]
print(driver(data), "GIBBS862131J99AA")  # 62
data = ["Andrew", "Robert", "Lee", "02-September-1981", "M"]
print(driver(data), "LEE99809021AR9AA")
