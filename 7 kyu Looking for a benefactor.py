def new_avg(arr, newavg):
    answer = newavg*float(len(arr) + 1) - sum(arr)
    if answer < 0:
        raise ValueError
    return int(answer + 0.999)



print(new_avg([14, 30, 5, 7, 9, 11, 16], 90), 628)
print(new_avg([14, 30, 5, 7, 9, 11, 15], 92), 645)
