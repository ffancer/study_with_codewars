def xor(a,b):
    return a ^ b


print(xor(False, False), False, "False xor False == False")
print(xor(True, False), True, "True xor False == True")
print(xor(False, True), True, "False xor True == True")
print(xor(True, True), False, "True xor True == False")
print(xor(False, xor(False, False)), False)
print(xor(xor(True, False), False), True)
print(xor(xor(True, True), False), False)
print(xor(True, xor(True, True)), True)
print(xor(xor(False, False), xor(False, False)), False)
print(xor(xor(False, False), xor(False, True)), True)
print(xor(xor(True, False), xor(False, False)), True)
print(xor(xor(True, False), xor(True, False)), False)
print(xor(xor(True, True), xor(True, False)), True)
print(xor(xor(True, xor(True, True)), xor(xor(True, True), False)), True)