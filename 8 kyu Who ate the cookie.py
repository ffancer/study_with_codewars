# 8 kyu
# Who ate the cookie?

def cookie(x):
    return f'Who ate the last cookie? It was {"Zach" if type(x) is str else "Monica" if type(x) in [int, float] else "the dog"}!'


print(cookie("Ryan"), "Who ate the last cookie? It was Zach!")
print(cookie(2.3), "Who ate the last cookie? It was Monica!")
print(cookie(26), "Who ate the last cookie? It was Monica!")
print(cookie(True), "Who ate the last cookie? It was the dog!")
