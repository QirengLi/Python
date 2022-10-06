def productExceptSelf(nums):
    left_nums, right_nums, res = [1] * len(nums), [1] * len(nums), [1] * len(nums)

    for i in range(1, len(nums)):
        left_nums[i] = nums[i - 1] * left_nums[i - 1]

    for i in reversed(range(len(nums) - 1)):
        right_nums[i] = nums[i + 1] * right_nums[i + 1]

    for i in range(len(nums)):
        res[i] = left_nums[i] * right_nums[i]

    return res
