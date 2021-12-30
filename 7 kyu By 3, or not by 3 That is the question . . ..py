# 7 kyu
# By 3, or not by 3? That is the question . . .


def divisible_by_three(st):
    lst = []

    for i in range(0, 500, 3):
        lst.append(i)

    total = 0

    for i in st:
        total += int(i)

    return total in lst



print(divisible_by_three('123'), True,
      "Should return true if the sum of the given digits is divisible by 3.")
print(divisible_by_three('19254'), True,
      "Should return true if the sum of the given digits is divisible by 3.")
print(divisible_by_three('88'), False,
      "Should return false if the sum of the given digits is not divisible by 3.")
print(divisible_by_three('1'), False,
      "Should return false if the sum of the given digits is not divisible by 3")
