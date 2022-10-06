def productExceptSelf(nums):

# Left array to contain
    left_nums, right_nums, res = [1] * len(nums), [1] * len(nums), [1] * len(nums)

# Iteration/step - Left nums array
# input array - nums = [4, 5, 1, 8, 2]
# left_nums = [1, 1, 1, 1, 1]
# left_nums[0] = [1]
# left_nums[1] = nums[1 - 1] * left_nums[1 - 1] = [4] * [1] = 4
# left_nums[2] = nums[2 - 1] * left_nums[2 - 1] = [5] * [4] = 20
# left_nums[3] = nums[3 - 1] * left_nums[3 - 1] = [1] * [20] = 20
# left_nums[4] = nums[4 - 1] * left_nums[4 - 1] = [8] * [20] = 160
# left_nums = [1, 4, 20, 20, 160]

    for i in range(1, len(nums)):
        left_nums[i] = nums[i - 1] * left_nums[i - 1]

# Work backwards in array ( right to left )
# Iteration/step - Right nums array
# input array - nums = [4, 5, 1, 8, 2]
# right_nums = [1, 1, 1, 1, 1]
# right_nums[4] = nums[4 + 1] * right_nums[4 + 1] = [1] * [1] = 1
# right_nums[3] = nums[3 + 1] * right_nums[3 + 1] = [2] * [1] = 2
# right_nums[2] = nums[2 + 1] * right_nums[2 + 1] = [8] * [2] = 16
# right_nums[1] = nums[1 + 1] * right_nums[1 + 1] = [1] * [16] = 16
# right_nums[0] = nums[0 + 1] * right_nums[0 + 1] = [5] * [16] = 80
# right_nums = [80, 16, 16, 2, 1]

    for i in reversed(range(len(nums) - 1)):
        right_nums[i] = nums[i + 1] * right_nums[i + 1]

# input array - nums = [4, 5, 1, 8, 2]
# left_nums = [1, 4, 20, 20, 160]
# right_nums = [80, 16, 16, 2, 1]
# res = [1, 1, 1, 1, 1]
# res[0] = left_nums[0] * right_nums[0] = [1] * [80] = 80
# res[1] = left_nums[1] * right_nums[1] = [4] * [16] = 64
# res[2] = left_nums[2] * right_nums[2] = [20] * [16] = 320
# res[3] = left_nums[3] * right_nums[3] = [20] * [2] = 40
# res[4] = left_nums[4] * right_nums[4] = [1] * [160] = 160
# res[] = [80, 64, 320, 40, 160]

    for i in range(len(nums)):
        res[i] = left_nums[i] * right_nums[i]

    return res

# Time Complexity O(n)
# Space Complexity O(n)


# More optimized version that uses a better space complexity
def productExceptSelfTwo(nums):
    res = [1] * (len(nums))

    currProduct = 1
    for i in range(len(nums)):
        res[i] = currProduct
        currProduct *= nums[i]

    currProduct = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= currProduct
        currProduct *= nums[i]

    return res

# Time Complexity O(n)
# Space Complexity O(1)
