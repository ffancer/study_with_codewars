def evens_and_odds(n):
    return bin(n) if n % 2 ==0 else hex(n)


print(evens_and_odds(2), '10')
print(evens_and_odds(13), 'd')
