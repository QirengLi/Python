def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        ans = numbers[left] + numbers[right]

        if ans == target:
            return [left + 1, right + 1]
        elif ans < target:
            left += 1
        else:
            right -= 1

            