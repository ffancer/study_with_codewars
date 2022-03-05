def fizz_buzz_cuckoo_clock(time):
    time = time.split(':')
    time = [int(i) for i in time]
    hour = time[0]
    minute = time[1]
    # if minute == 0:
    #     return 'Cuckoo' * hour
    # if minute == 30:
    #     return 'Cuckoo'
    if minute % 15 == 0:
        return "Fizz Buzz"
    if minute % 3 == 0:
        return "Fizz"
    if minute % 5 == 0:
        return "Buzz"

print(fizz_buzz_cuckoo_clock("13:34"), "tick")
print(fizz_buzz_cuckoo_clock("21:00"), "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo")
print(fizz_buzz_cuckoo_clock("11:15"), "Fizz Buzz")
print(fizz_buzz_cuckoo_clock("03:03"), "Fizz")
print(fizz_buzz_cuckoo_clock("14:30"), "Cuckoo")
print(fizz_buzz_cuckoo_clock("08:55"), "Buzz")
print(fizz_buzz_cuckoo_clock("00:00"),
      "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo")
print(fizz_buzz_cuckoo_clock("12:00"),
      "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo")
