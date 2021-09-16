# 8 kyu
# Exclamation marks series #6: Remove n exclamation marks in the sentence from left to right
def remove(s, n):
    return s.replace("!", "", n)





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







