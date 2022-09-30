def uniqueOccurrences(arr):
    if not arr:
        return False

    hashm = {}

    for num in arr:

        if num in hashm:
            hashm[num] += 1
        else:
            hashm[num] = 1

    return len(hashm) == len(set(hashm.values()))
