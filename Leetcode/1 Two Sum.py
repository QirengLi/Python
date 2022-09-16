def twoSum(nums, target):

    # Space Complexity: O(n)
    # Time Complexity: O(n)
    dict = {}

    for i, n in enumerate(nums):

        # value of nums -> index of value of nums
        diff = target - n

        # if diff of target is in dictionary, then we return the index of the difference
        # and the current iteration/index
        # else it will add the current number to dictionary as the key, and it's index as the value
        if diff in dict:
            return [dict[diff], i]
        dict[n] = i
