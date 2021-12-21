def solve(a, b):
    s = ''

    for i in a:
        if i not in b:
            s += i

    for j in b:
        if j not in a:
            s += j

    return s



print(solve("xyab", "xzca"), "ybzc")
print(solve("xyabb", "xzca"), "ybbzc")
print(solve("abcd", "xyz"), "abcdxyz")
print(solve("xxx", "xzca"), "zca")
