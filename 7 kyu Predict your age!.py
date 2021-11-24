def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    multiply_and_sum = age_1 ** 2 + age_2 ** 2 + age_3 ** 2 + age_4 ** 2 + age_5 ** 2 + age_6 ** 2 + age_7 ** 2 + age_8 ** 2
    squre_root = multiply_and_sum ** 0.5
    divide_by_two = squre_root // 2

    return int(divide_by_two)

print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))
