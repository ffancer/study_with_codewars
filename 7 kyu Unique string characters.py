def solve(a, b):
    s = ''
    for i in a:
        if i in b:
            continue
        else:
            s += i

    return s

print(solve("xyab", "xzca"), "ybzc")
print(solve("xyabb", "xzca"), "ybbzc")
print(solve("abcd", "xyz"), "abcdxyz")
print(solve("xxx", "xzca"), "zca")
