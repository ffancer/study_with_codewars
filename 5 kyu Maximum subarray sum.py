def max_sequence(arr):
    minimum, total, answer = 0, 0, 0

    for i in range(len(arr)):
        total += arr[i]
        minimum = min(total, minimum)
        answer = max(answer, total - minimum)

    return answer


print(max_sequence([]), 0)
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
