def balanced_num(number):
    num = str(number)
    left = num[:int(len(num))//2]
    right = num[int(len(num))//2::]
    return


print(balanced_num(7), "Balanced")
print(balanced_num(959), "Balanced")
print(balanced_num(13), "Balanced")
print(balanced_num(432), "Not Balanced")
print(balanced_num(424), "Balanced")

print(balanced_num(1024), "Not Balanced")
print(balanced_num(66545), "Not Balanced")
print(balanced_num(295591), "Not Balanced")
print(balanced_num(1230987), "Not Balanced")
print(balanced_num(56239814), "Balanced")