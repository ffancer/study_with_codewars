def final_grade(exam, projects):
    answer = 0

    if exam > 90 or projects > 10:
        answer = 100
    elif exam > 75 and projects >= 5:
        answer = 90
    elif exam > 50 and projects >= 2:
        answer = 75

    return answer


print(final_grade(100, 12), 100)
print(final_grade(85, 5), 90)