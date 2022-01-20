def solution(s):
    if len(s) % 2 != 0:
        return '____'
    lst = [s[i:i+2] for i in range(0, len(s), 2)]
    return lst

print(solution("asdfadsf"), ['as', 'df', 'ad', 'sf'])
print(solution("asdfads"), ['as', 'df', 'ad', 's_'])
print(solution(""))
print(solution("x"), ["x_"])
