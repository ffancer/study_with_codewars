def solve(a, b):
    c = a + b

    for i in c:
        if c.count(i) >= 2:
            c = c.replace(i, '')

    return c



print(solve("xyab", "xzca"), "ybzc")
print(solve("xyabb", "xzca"), "ybbzc")
print(solve("abcd", "xyz"), "abcdxyz")
print(solve("xxx", "xzca"), "zca")
