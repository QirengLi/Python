def maxSubArray(nums):
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(0, current_sum + num)

        # The above max function will reset the subarray if the sum is negative

        max_sum = max(max_sum, current_sum)
    return max_sum

# Kadane's Algorithm

def maxSubArray(nums):
    current_sum = 0
    max_sum = nums[0]

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0
        # similar to above algorithm where if current sum is negative, it will reset to 0

    return max_sum

# Different version of Kadane's Algorithm
