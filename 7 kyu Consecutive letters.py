def solve(st):
    for i in st:
        if st.count(i) > 1:
            return False


print(solve("abc"), True)
print(solve("abd"), False)
print(solve("dabc"), True)
print(solve("abbc"), False)
