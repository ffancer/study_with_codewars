def calculator(txt):
    a, operator, b = txt.split()
    a, b = len(a), len(b)

    def erithmetic(a, b, operator):
        return {
            '+': a + b,
            '-': a - b,
            '//': a // b,
            '*': a * b
        }[operator]


print(calculator("..... + ..............."), "....................")
print(calculator("..... - ..."), "..")
print(calculator("..... - ."), "....")
print(calculator("..... * ..."), "...............")
print(calculator("..... * .."), "..........")
print(calculator("..... // .."), "..")
print(calculator("..... // ."), ".....")
print(calculator(". // .."), "")
print(calculator(". - ."), "")
