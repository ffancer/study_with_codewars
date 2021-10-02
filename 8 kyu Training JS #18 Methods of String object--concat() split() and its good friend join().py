# 8 kyu
# Training JS #18: Methods of String object--concat() split() and its good friend join()

# def split_and_merge(string_, separator):
#     # return separator.join(list(string_))
#     return '-'.join(list(string_))


def split_and_merge(string_, separator):
    return ' '.join(separator.join(j for j in i) for i in string_.split())



print(split_and_merge("My name is John", " "), "M y n a m e i s J o h n")
print(split_and_merge("My name is John", "-"), "M-y n-a-m-e i-s J-o-h-n")
print(split_and_merge("Hello World!", "."), "H.e.l.l.o W.o.r.l.d.!")
print(split_and_merge("Hello World!", ","), "H,e,l,l,o W,o,r,l,d,!")
