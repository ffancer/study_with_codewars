# 8 kyu
# Who ate the cookie?

def cookie(x):
    answer = 'the dog'

    if type(x) == str:
        answer = 'Zach'
    elif type(x) == int or type(x) == float:
        answer = 'Monica'

    return f"Who ate the last cookie? It was {answer}!"


print(cookie("Ryan"), "Who ate the last cookie? It was Zach!")
print(cookie(2.3), "Who ate the last cookie? It was Monica!")
print(cookie(26), "Who ate the last cookie? It was Monica!")
print(cookie(True), "Who ate the last cookie? It was the dog!")