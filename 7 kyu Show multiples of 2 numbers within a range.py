# Python version: return multiples of 2 numbers in a list
def multiples(s1, s2, s3):
    return []


s1, s2, s3 = 2, 4, 40
print(s1, s2, s3)
print(multiples(s1, s2, s3), [4, 8, 12, 16, 20, 24, 28, 32, 36])

s1, s2, s3 = 3, 4, 40
print(s1, s2, s3)
print(multiples(s1, s2, s3), [12, 24, 36])

s1, s2, s3 = 7, 4, 80
print(s1, s2, s3)
print(multiples(s1, s2, s3), [28, 56])

s1, s2, s3 = 7, 4, 20
print(s1, s2, s3)
print(multiples(s1, s2, s3), [])
