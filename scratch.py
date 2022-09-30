def uniqueOccurrences(arr):
    if not arr:
        return False

    hashm = {}

    for num in arr:
        if num in hashm:
            hashm[num] += 1
        else:
            hashm[num] = 1
    print(hashm)
    print(len(hashm))
    print(hashm.values())
    print(len(hashm.values()))
    print(set(hashm.values()))
    print(len(set(hashm.values())))
    return len(hashm) == len(set(hashm.values()))

uniqueOccurrences([1,2,2,1,1,3,4])