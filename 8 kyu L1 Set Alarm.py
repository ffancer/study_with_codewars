# 8 kyu
# L1: Set Alarm

def set_alarm(employed, vacation):
    if employed == vacation:
        return False
    elif not employed and vacation:
        return False
    elif employed and not vacation:
        return True


print(set_alarm(True, True), False, "Fails when input is True, True")
print(set_alarm(False, True), False, "Fails when input is False, True")
print(set_alarm(False, False), False, "Fails when input is False, False")
print(set_alarm(True, False), True, "Fails when input is True, False")
