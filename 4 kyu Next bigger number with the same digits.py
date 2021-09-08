def next_bigger(n):
    answer = -1

    if len(str(n)) == 2:
        if int(str(n)[0]+str(n)[1]) > int(str(n)[1]+str(n)[0]):
            answer = int(str(n)[0]+str(n)[1])
        else:
            answer = int(str(n)[1]+str(n)[0])

    return answer



print(next_bigger(12),21)
# print(next_bigger(513),531)
# print(next_bigger(2017),2071)
# print(next_bigger(414),441)
# print(next_bigger(144),414)