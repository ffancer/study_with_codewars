def validate_code(code):
    flag = True
    if str(code)[0] not in '123' or str(code)[1] not in '123' or str(code)[2] not in '123':
        flag = False
    return flag

print(validate_code(123), True)
print(validate_code(248), True)
print(validate_code(8), False)
print(validate_code(321), True)
print(validate_code(9453), False)
