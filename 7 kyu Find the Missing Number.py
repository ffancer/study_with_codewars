def missing_no(nums):
    return 100 * 101 // 2 - sum(nums)


def examples():
    # Numbers from 0 to 100, but missing 5
    nums = list(range(0, 101))
    nums.remove(5)
    print(missing_no(nums), 5)

    nums = list(reversed(range(0, 101)))
    nums.remove(10)
    print(missing_no(nums), 10)


print(examples())
