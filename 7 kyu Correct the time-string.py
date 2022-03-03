def time_correct(t):
    try:
        if t == "":
            return ""
        if len(t) != 8:
            return None
        h, m, s = [int(x) for x in t.split(":")]
        if s >= 60:
            s -= 60
            m += 1
        if m >= 60:
            m -= 60
            h += 1
        if h >= 24:
            h = h % 24
        return '%02d:%02d:%02d' % (h, m, s)
    except:
        return None


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
