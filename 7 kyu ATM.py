def solve(n):
    cnt = 0

    while n > 500:
            n = n % 500
            cnt += 1

    return cnt, n


print(solve(770), 4, "Wrong result for 770")
print(solve(550), 2, "Wrong result for 550")
print(solve(10), 1, "Wrong result for 10")
print(solve(1250), 4, "Wrong result for 1250")
print(solve(1500), 3, "Wrong result for 1500")
print(solve(125), -1, "Wrong result for 125")
print(solve(666), -1, "Wrong result for 666")
print(solve(42), -1, "Wrong result for 42")
