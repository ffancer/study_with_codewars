# 7 kyu
# Coding 3min : Remove screws I


def sc(s):
    i, j = 0, 1
    time = 1

    while j < len(s):
        if s[i] != s[j]:
            time += 5
        time += 2
        i += 1
        j += 1

    return time


print(sc("+"), 1)
print(sc("-"), 1)
print(sc("+-"), 8)
print(sc("-+"), 8)
print(sc("---+++"), 16)
print(sc("-+-+-+"), 36)
print(sc("-+-+-----------"), 49)
print(sc("-+-+-++++++++++"), 54)
