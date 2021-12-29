def new_avg(arr, newavg):
    return (len(arr) + 1) * newavg - sum(arr)


print(new_avg([14, 30, 5, 7, 9, 11, 16], 90), 628)
print(new_avg([14, 30, 5, 7, 9, 11, 15], 92), 645)
