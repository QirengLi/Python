def numIdenticalPairs(nums):
    hashm = {}
    count = 0

    for num in nums:
        if num in hashm:
            count += hashm[num]
            hashm[num] += 1
        else:
            hashm[num] = 1
    return count
