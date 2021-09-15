def validate_usr(username):
    cnt = 0

    if 4 <= len(username) <= 16:
        cnt += 1
    elif username.islower():
        cnt += 1
    elif username.isdigit():
        cnt += 1
    elif '_' in username:
        cnt += 1
    if cnt == 4:
        return True
    return False


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