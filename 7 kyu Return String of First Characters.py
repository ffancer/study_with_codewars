def make_string(s):
    s = s.split()
    answer = ''

    for i in s:
        answer += i[0]

    return answer

print(make_string("sees eyes xray yoat"), "sexy", "Wrong result for 'sees eyes xray yoat'")
print(make_string("brown eyes are nice"), "bean", "Wrong result for 'brown eyes are nice'")
print(make_string("cars are very nice"), "cavn", "Wrong result for 'cars are very nice'")
print(make_string("kaks de gan has a big head"), "kdghabh", "Wrong result for 'kaks de gan has a big head'")
