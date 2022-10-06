def productExceptSelf(nums):

# Left array to contain
    left_nums, right_nums, res = [1] * len(nums), [1] * len(nums), [1] * len(nums)

    for i in range(1, len(nums)):
        left_nums[i] = nums[i - 1] * left_nums[i - 1]

    for i in reversed(range(len(nums) - 1)):
        right_nums[i] = nums[i + 1] * right_nums[i + 1]

    for i in range(len(nums)):
        res[i] = left_nums[i] * right_nums[i]

    return res
# Time Complexity O(n)
# Space Complexity O(n)

# More optimized version that uses a better space complexity
# Time Complexity O(n)
# Space Complexity O(1)

def productExceptSelfTwo(nums):
    res = [1] * (len(nums))

    left = 1
    for i in range(len(nums)):
        res[i] = left
        left *= nums[i]
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res
