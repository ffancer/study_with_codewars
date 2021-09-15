def validate_usr(username):
    if len(username) < 4 or len(username) > 16:
        return False

    allowed = 'abcdefghijklmnopqrstuvwxyz0123456789_'

    for i in username:
        if i not in allowed:
            return False
    return True


print(validate_usr('asddsa'), True)
print(validate_usr('a'), False)
print(validate_usr('Hass'), False)
print(validate_usr('Hasd_12assssssasasasasasaasasasasas'), False)
print(validate_usr(''), False)
print(validate_usr('____'), True)
print(validate_usr('012'), False)
print(validate_usr('p1pp1'), True)
print(validate_usr('asd43 34'), False)
print(validate_usr('asd43_34'), True)
print(validate_usr('pRt_286ji6u9Il_M'), False)
print(validate_usr('2ctds?45d'), False)
