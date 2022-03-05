def fizz_buzz_cuckoo_clock(time):
    time = time.split(':')
    time = [int(i) for i in time]
    hour = time[0]
    minute = time[1]
    clock = {0: 12, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 1, 14: 2, 15: 3, 16: 4, 17: 5, 18: 6, 19: 7, 20: 8, 21: 9, 22: 10, 23: 11, 24: 12}
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
