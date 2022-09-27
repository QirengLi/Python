# An array of boolean values is divided into two sections; the left section consists
# of all false and the right section consists of all true. Find the boundary of the right
# section, i.e. the index of the first true element. If there is no true element, return -1.

# Input: arr = [false, false, true, true, true]

# Output: 2
# Explanation: first true's index is 2.


def find_boundary(arr):
    left = 0
    right = len(arr) - 1
    res = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid]:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res
