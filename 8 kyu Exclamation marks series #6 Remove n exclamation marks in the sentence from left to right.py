# 8 kyu
# Exclamation marks series #6: Remove n exclamation marks in the sentence from left to right
def remove(s, n):
    answer = s[:n] + s[n+1:]

    return answer





print(remove("Hi!", 1))
print(remove("Hi!", 100))
print(remove("Hi!!!", 1))
print(remove("Hi!!!", 100))
print(remove("!Hi", 1))
print(remove("!Hi!", 1))
print(remove("!Hi!", 100))
print(remove("!!!Hi !!hi!!! !hi", 1))
print(remove("!!!Hi !!hi!!! !hi", 3))
print(remove("!!!Hi !!hi!!! !hi", 5))
print(remove("!!!Hi !!hi!!! !hi", 100))







