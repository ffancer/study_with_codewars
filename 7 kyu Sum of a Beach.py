def sum_of_a_beach(beach):  # "Sand", "Water", "Fish", and "Sun"
    beach = beach.lower()
    cnt = 0
    i = 5
    while i < len(beach):
        for i in ["sun", "sand", "fish", "water"]:
            if i in beach[:i]:
                cnt += 1
                i += 1

    return cnt


print(sum_of_a_beach("SanD"), 1)
print(sum_of_a_beach("sunshine"), 1)
print(sum_of_a_beach("sunsunsunsun"), 4)
print(sum_of_a_beach("123FISH321"), 1)