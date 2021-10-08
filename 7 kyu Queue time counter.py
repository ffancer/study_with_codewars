def queue(queuers,pos):
    cnt = 0

    while queuers[pos] > 0:
        if pos == 0:
            pos = len(queuers) - 1
        else:
            pos -= 1
        queuers[0] -= 1
        queuers.append(queuers[0])
        queuers.pop(0)
        cnt += 1

    return cnt + sum([i for i in queuers if i < 0])


print(queue([2, 5, 3, 6, 4], 0), 6)
print(queue([2, 5, 3, 6, 4], 1), 18)
print(queue([2, 5, 3, 6, 4], 2), 12)
print(queue([2, 5, 3, 6, 4], 3), 20)
print(queue([2, 5, 3, 6, 4], 4), 17)
