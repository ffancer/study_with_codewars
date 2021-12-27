def solution(stones):
    cnt = 0

    for i in range(len(stones) - 1):
        if stones[i] == stones[i + 1]:
            cnt += 1

    return cnt

print(solution("RGBRGBRGGB"), 1)
print(solution("RGGRGBBRGRR"), 3)
print(solution("RRRRGGGGBBBB"), 9)
