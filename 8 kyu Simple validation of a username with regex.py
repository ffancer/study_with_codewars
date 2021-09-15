def validate_usr(username):

    if len(username) >= 17 or len(username) <= 3:
        return False
    if username.isupper():
        return False
    if ' ' in username:
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