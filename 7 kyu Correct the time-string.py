def time_correct(t):
    pass


print(time_correct(None), None)
print(time_correct(""), "")
print(time_correct("001122"), None)
print(time_correct("00;11;22"), None)
print(time_correct("0a:1c:22"), None)
print(time_correct("09:10:01"), "09:10:01")
print(time_correct("11:70:10"), "12:10:10")
print(time_correct("19:99:99"), "20:40:39")
print(time_correct("24:01:01"), "00:01:01")
print(time_correct("52:01:01"), "04:01:01")