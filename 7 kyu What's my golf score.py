# 7 kyu
# What's my golf score?


def golf_score_calculator(par_string, score_string):
    return sum(int(j) - int(i) for i, j in zip(par_string, score_string))


print(golf_score_calculator('443454444344544443', '353445334534445344'), -1)
