def solve(s):
    upper_cnt, lower_cnt, num_cnt, special_cnt = 0, 0, 0, 0

    for i in s:
        if i.isupper():
            upper_cnt += 1
        if i.islower():
            lower_cnt += 1
        if i.isdigit():
            num_cnt += 1
        else:
            special_cnt += 1

    return [upper_cnt, lower_cnt, num_cnt, special_cnt]


print(solve("Codewars@codewars123.com"), [1, 18, 3, 2])
print(solve("bgA5<1d-tOwUZTS8yQ"), [7, 6, 3, 2])
print(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"), [9, 9, 6, 9])
print(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"), [15, 8, 6, 9])
print(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe"), [10, 7, 3, 6])
print(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"), [7, 13, 4, 10])
