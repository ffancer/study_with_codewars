def special_number(number):
    for i in str(number):
        if i in ['0', '1', '2', '3', '4', '5']:
            continue
        return "NOT!!"
    return "Special!!"


print(special_number(2), "Special!!")
print(special_number(5), "Special!!")
print(special_number(9), "NOT!!")
print(special_number(7), "NOT!!")
print(special_number(23), "Special!!")
print(special_number(79), "NOT!!")
print(special_number(39), "NOT!!")
print(special_number(55), "Special!!")
print(special_number(513), "Special!!")
print(special_number(709), "NOT!!")
print(special_number(970569), "NOT!!")
print(special_number(11350224), "Special!!")
