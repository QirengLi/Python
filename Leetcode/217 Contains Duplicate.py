def containsDuplicate(nums):

    # Space Complexity: O(n)
    # Time Complexity: O(n)

    # hashset or dictionary for optimal lookup
    hashset = set()

    # First found duplicate will end function and return true since it satisfies the requirements
    # and won't need to continue the for loop
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)

    # Will return false once for loop goes through every item therefore not containing any duplicates
    return False