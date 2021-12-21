def solve(n):
    if n % 10:
        return -1

    cnt = 0
    money = [500, 200, 100, 50, 20, 10]

    for i in money:
        while n >= i:
            n -= i
            cnt += 1

    return cnt


print(solve(770), 4, "Wrong result for 770")
print(solve(550), 2, "Wrong result for 550")
print(solve(10), 1, "Wrong result for 10")
print(solve(1250), 4, "Wrong result for 1250")
print(solve(1500), 3, "Wrong result for 1500")
print(solve(125), -1, "Wrong result for 125")
print(solve(666), -1, "Wrong result for 666")
print(solve(42), -1, "Wrong result for 42")
