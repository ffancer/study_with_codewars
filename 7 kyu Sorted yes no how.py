def is_sorted_and_how(arr):
    answer = 'no'

    if arr == sorted(arr):
        answer = 'yes, ascending'
    elif arr == sorted(arr, reverse=True):
        answer = 'yes, descending'

    return answer


print(is_sorted_and_how([1, 2]))  # 'yes, ascending'
print(is_sorted_and_how([15, 7, 3, -8]))  # 'yes, descending'
print(is_sorted_and_how([4, 2, 30]))  # no
