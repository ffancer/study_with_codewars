# best practice 1:
def is_lucky(n):
    return n % 9 == 0


# best practice 2:
def is_lucky(n):
    digits = list(str(n))
    return sum(list(map(int, digits))) % 9 == 0


# best practice 3:
def is_lucky(n):
    return sum([int(i) for i in str(n)]) % 9 == 0


print(is_lucky(1892376), True, "Wrong result for 1892376")
print(is_lucky(189237), False, "Wrong result for 189237")
print(is_lucky(18922314324324234423437), False, "Wrong result for 18922314324324234423437")
print(is_lucky(189223141324324234423437), True, "Wrong result for 189223141324324234423437")
print(is_lucky(1892231413243242344321432142343423437), True, "Wrong result for 1892231413243242344321432142343423437")
print(is_lucky(0), True, "Wrong result for 0")
