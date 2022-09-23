def firstBadVersion(n):
    low = 1 # use 1 here because it's based on "versions" and realistically wouldn't have a version 0
    high = n

    while low < high:
        mid = low + (high - low) // 2 # adding low after calculating "true mid" (( high-low) // 2) helps avoid overflow

        if isBadVersion(mid): #Assuming IsBadVersion(version) checks and returns bool value if version is bad
            high = mid
        else:
            low = mid + 1
    return low
