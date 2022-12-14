# Given a sorted array of integers and a target integer, find the first
# occurrence of the target and return its index. Return -1 if the target is not in the array.

# Input:
# arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
# target = 3
# Output: 1
# Explanation: First occurrence of 3 is at index 1.

# Input:
# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# target = 6
# Output: -1
# Explanation: 6 does not exists in the array

def find_first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    res = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            res = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return res
