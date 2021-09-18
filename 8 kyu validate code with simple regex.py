def validate_code(code):
    for i in str(code):
        if i in '123':
            return True
        return False

print(validate_code(123), True)
print(validate_code(248), True)
print(validate_code(8), False)
print(validate_code(321), True)
print(validate_code(9453), False)
