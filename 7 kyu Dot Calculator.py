def calculator(txt):
    a, operator, b = txt.split()
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
