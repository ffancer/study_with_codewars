def disarium_number(number):
    num = str(number)
    lst = []

    for i in range(len(num)):
        lst.append(int(num[i]) ** int(i+1))

    return "Disarium !!" if sum(lst) == number else "Not !!"


print(disarium_number(89), "Disarium !!")
print(disarium_number(518), "Disarium !!")
print(disarium_number(1024), "Not !!")
