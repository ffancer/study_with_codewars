# 8 kyu
# Training JS #18: Methods of String object--concat() split() and its good friend join()

# first
def split_and_merge(string, sp):
    return ' '.join(sp.join(word) for word in string.split())

# second
def split_and_merge(s, sp):
    return ' '.join(sp.join(i) for i in s.split())


print(split_and_merge("My name is John", " "), "M y n a m e i s J o h n")
print(split_and_merge("My name is John", "-"), "M-y n-a-m-e i-s J-o-h-n")
print(split_and_merge("Hello World!", "."), "H.e.l.l.o W.o.r.l.d.!")
print(split_and_merge("Hello World!", ","), "H,e,l,l,o W,o,r,l,d,!")
