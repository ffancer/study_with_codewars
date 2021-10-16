# 8 kyu
# Did she say hallo?

def validate_hello(greetings):
    #your code here

print(validate_hello('hello'), True)
print(validate_hello('ciao bella!'), True)
print(validate_hello('salut'), True)
print(validate_hello('hallo, salut'), True)
print(validate_hello('hombre! Hola!'), True)
print(validate_hello('Hallo, wie geht\'s dir?'), True)
print(validate_hello('AHOJ!'), True)
print(validate_hello('czesc'), True)
print(validate_hello('meh'), False)
print(validate_hello('Ahoj'), True)