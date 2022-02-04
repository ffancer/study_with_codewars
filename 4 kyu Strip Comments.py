def solution(string, markers):
    s = string.split('\n')
    answer = ''

    for i in s:
        length = len(i)
        for j, k in enumerate(i):
            if k in markers:
                length = j
                break
        answer += i[:length].strip() + '\n'

    return answer[:-1]


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
print(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
