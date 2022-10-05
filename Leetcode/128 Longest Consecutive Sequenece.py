def longestConsecutive(nums):

    numSet = set(nums)
    maxLength = 0

    #Keep track of the longest consecutive sequence

    for num in nums:
        # If statement checks for the beginning sequence number by checking
        # the number before it to see if it exists

        if (num - 1) not in numSet:
            # currLength to refresh and keep track of the current sequence
            currLength = 0
            # condition increments the number if there are sequential numbers ( 1, 2, 3)
            while (num + currLength) in numSet:
                currLength += 1
            maxLength = max(currLength, maxLength)
    return maxLength

