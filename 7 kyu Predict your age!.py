def predict_age(*ages):
    return int(sum(i * i for i in ages) ** 0.5 // 2)


print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))
