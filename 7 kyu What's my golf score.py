# 7 kyu
# What's my golf score?


def golf_score_calculator(par_string, score_string):
    lst_1 = [int(i) for i in par_string]
    lst_2 = [int(i) for i in score_string]
    ans = [y - x for x, y in zip(lst_1, lst_2)]
    return sum(ans)


print(golf_score_calculator('443454444344544443', '353445334534445344'), -1)
