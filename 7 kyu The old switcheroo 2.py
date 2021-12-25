def encode(string):
    s = ''

    for i in string.lower():
        if i.isalpha():
            s += str(ord(i)-96)
        else:
            s += i

    return s


print(encode('abc'), '123')
print(encode('ABCD'), '1234')
print(encode('ZzzzZ'), '2626262626')
print(encode('abc-#@5'), '123-#@5')
print(encode('this is a long string!! Please [encode] @C0RrEctly'),
      '208919 919 1 1215147 1920189147!! 161251195 [51431545] @30181853201225')
