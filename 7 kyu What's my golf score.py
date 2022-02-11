# 7 kyu
# What's my golf score?


def golf_score_calculator(par_string, score_string):
    total = 0
    for i in par_string:
        for j in score_string:
            total += int(i) - int(j)

    return total


print(golf_score_calculator('443454444344544443', '353445334534445344'), -1)
