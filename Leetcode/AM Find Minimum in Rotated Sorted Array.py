# A sorted array of unique integers was rotated at an unknown pivot.
# For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20].
# Find the index of the minimum element in this array. All the numbers are unique.

# Input: [30, 40, 50, 10, 20]
# Output: 3
# Explanation: the smallest element is 10 and its index is 3.

# Input: [3, 5, 7, 11, 13, 17, 19, 2]
# Output: 7
# Explanation: the smallest element is 2 and its index is 7.

def find_min_rotated(arr):
    left = 0
    right = len(arr) - 1
    res = 0

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] <= arr[-1]:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

