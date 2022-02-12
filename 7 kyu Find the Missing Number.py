def missing_no(nums):
    try:
        nums_max, nums_min = max(nums), min(nums)
        lst = [i for i in range(nums_min, nums_max+1)]
        ans = ''

        for i in lst:
            if i not in nums:
                ans += str(i)

        return int(ans)
    except ValueError:
        return 0


def examples():
    # Numbers from 0 to 100, but missing 5
    nums = list(range(0, 101))
    nums.remove(5)
    print(missing_no(nums), 5)

    nums = list(reversed(range(0, 101)))
    nums.remove(10)
    print(missing_no(nums), 10)


print(examples())
