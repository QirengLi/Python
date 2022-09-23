def firstBadVersion(n):
    low = 0
    high = n - 1

    while low < high:
        mid = low + (high - low) // 2

        if isBadVersion(mid): #Assuming IsBadVersion(version) checks and returns bool value if version is bad
            high = mid
        else:
            low = mid + 1
    return low
