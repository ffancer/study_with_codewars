def sale_hotdogs(n):
    answer = 0

    if n < 5:
        answer = 100 * n
    elif 5 <= n < 10:
        answer = 95 * n
    elif n >= 10:
        answer = 90 * n

    return answer


print(sale_hotdogs(0), 0)
print(sale_hotdogs(1), 100)
print(sale_hotdogs(2), 200)
print(sale_hotdogs(3), 300)
print(sale_hotdogs(4), 400)
print(sale_hotdogs(5), 475)
print(sale_hotdogs(9), 855)
print(sale_hotdogs(10), 900)
print(sale_hotdogs(11), 990)
print(sale_hotdogs(100), 9000)
