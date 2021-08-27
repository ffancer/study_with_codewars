from math import floor

def odd_count(n):
    # first solution, but it's slow with huge num-s:
    # cnt = 0
    #
    # for i in range(1, n+1):
    #     if i > 0 and i % 2 == 0:
    #         cnt += 1
    #
    # return cnt

    # second solution
    # return len([i for i in range(1, n+1) if i > 0 and i % 2 == 0])

    # third solution
    return floor(n / 2)



print(odd_count(15), 7)
print(odd_count(15023), 7511)