from math import factorial


def strong_num(number):
    total = 0

    for i in str(number):
        total += factorial(int(i))
    return "STRONG!!!!" if total == number else "Not Strong !!"


print(strong_num(1), "STRONG!!!!")
print(strong_num(2), "STRONG!!!!")
print(strong_num(145), "STRONG!!!!")

print(strong_num(7), "Not Strong !!")
print(strong_num(93), "Not Strong !!")
print(strong_num(185), "Not Strong !!")
