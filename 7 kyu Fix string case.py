def solve(s):
    cnt_lowercase, cnt_uppercase = 0, 0

    for i in s:
        if i.islower():
            cnt_lowercase += 1
        elif i.isupper():
            cnt_uppercase += 1

    return s.lower() if cnt_lowercase == cnt_uppercase or cnt_lowercase > cnt_uppercase else s.upper()


print(solve("coDe"))
print(solve("CODe"))
print(solve("coDE"))
