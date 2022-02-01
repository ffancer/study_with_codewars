def sum_of_a_beach(beach):
    cnt = 0

    for i in ["sand", "water", "fish", "sun"]:
        if i in beach.lower():
            cnt += 1

    return cnt


print(sum_of_a_beach("SanD"), 1)
print(sum_of_a_beach("sunshine"), 1)
print(sum_of_a_beach("sunsunsunsun"), 4)
print(sum_of_a_beach("123FISH321"), 1)