def sum_of_minimums(numbers):
    # first:
    # total = 0
    #
    # for i in numbers:
    #     total += min(i)
    #
    # return total

    # second:
    return sum([min(i) for i in numbers])
