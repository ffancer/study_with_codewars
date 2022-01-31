def remainder(a, b):
    try:
        return max(a, b) % min(a, b)
    except ZeroDivisionError:
        return None


print(remainder(17, 5), 2,
      'Returned value should be the value left over after dividing as much as possible.')
print(remainder(13, 72), remainder(72, 13), 'The order the arguments are passed should not matter.')
print(remainder(1, 0), None, 'Divide by zero should return None')
print(remainder(0, 0), None, 'Divide by zero should return None')
print(remainder(0, 1), None, 'Divide by zero should return None')
print(remainder(-1, 0), 0, 'Divide by zero should only be checked for the lowest number')
print(remainder(0, -1), 0, 'Divide by zero should only be checked for the lowest number')
print(remainder(-13, -13), 0, 'Should handle negative numbers')
print(remainder(-60, 340), -20, 'Should handle negative numbers')
print(remainder(60, -40), -20, 'Should handle negative numbers')
