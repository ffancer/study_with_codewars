# best practice 1:
def validate_code(code):
    return str(code).startswith(('1', '2', '3'))


print(validate_code(123), True)
print(validate_code(248), True)
print(validate_code(8), False)
print(validate_code(321), True)
print(validate_code(9453), False)
