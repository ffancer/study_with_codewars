def solution(s):
    if len(s) % 2 != 0:
        return '____'


print(solution("asdfadsf"), ['as', 'df', 'ad', 'sf'])
print(solution("asdfads"), ['as', 'df', 'ad', 's_'])
print(solution(""))
print(solution("x"), ["x_"])
