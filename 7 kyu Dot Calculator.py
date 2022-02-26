def calculator(txt):
    a, operator, b = txt.split()
    a, b = len(a), len(b)
    return a, b, operator

print(calculator("..... + ..............."), "....................")
print(calculator("..... - ..."), "..")
print(calculator("..... - ."), "....")
print(calculator("..... * ..."), "...............")
print(calculator("..... * .."), "..........")
print(calculator("..... // .."), "..")
print(calculator("..... // ."), ".....")
print(calculator(". // .."), "")
print(calculator(". - ."), "")
