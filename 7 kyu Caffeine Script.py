def caffeine_buzz(n):
    if n % 3 == 0 and n % 4 == 0 and n % 2 == 0:
        return 'CoffeeScript'
    if n % 3 == 0 and n % 2 == 0:
        return 'JavaScript'
    if n % 3 == 0:
        return 'Java'
    if n % 3 == 0 and n % 4 == 0:
        return 'Coffee'
    return "mocha_missing!"


print(caffeine_buzz(1), "mocha_missing!")
print(caffeine_buzz(2), "mocha_missing!")
print(caffeine_buzz(3), "Java")
print(caffeine_buzz(4), "mocha_missing!")
print(caffeine_buzz(5), "mocha_missing!")
print(caffeine_buzz(6), "JavaScript")
print(caffeine_buzz(7), "mocha_missing!")
print(caffeine_buzz(8), "mocha_missing!")
print(caffeine_buzz(9), "Java")
print(caffeine_buzz(10), "mocha_missing!")
print(caffeine_buzz(11), "mocha_missing!")
print(caffeine_buzz(12), "CoffeeScript")
