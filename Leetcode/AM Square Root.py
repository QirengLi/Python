# Given an integer, find its square root without using the built-in square root
# function. Only return the integer part (truncate the decimals).

# Input: 16
# Output: 4

# Input: 8
# Output: 2
# Explanation: square root of 8 is 2.83..., return integer part 2

def square_root(n):
    left = 1
    right = n
    res = 0

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= n:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res
