def solution(string, markers):
    return string.split('\n')


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
print(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
