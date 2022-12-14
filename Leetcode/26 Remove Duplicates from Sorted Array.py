def removeDuplicates(nums):
    if not nums:
        return 0
    count = 0
    for i in range(len(nums)):
        if nums[i] != nums[count]:
            count += 1
            nums[count] = nums[i]
    return count + 1

# "+ 1" to account for difference in index
# Fast and slow pointer approach
# var count = slow pointer and to track the 'k' amount of elements
# for loop 'i' = fast pointer
