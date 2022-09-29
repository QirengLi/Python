# Recursion is a function that will call itself until a condition is met
# usually by its "base" or "default" case
# For example, take going to the gym and weight lost as an example.
# We will go to the gym until we lose an x amount of weight or until we meet
# a certain weight goal.
# In code, it would look like this.
def go_to_gym(goal_weight):
    if goal_weight == 180:
        return "Base/default case met! recursive loop ends here!"
    else:
        return go_to_gym(goal_weight - 1)
# print(go_to_gym(200))


# 1.) Write a program to calculate the sum of a list of numbers
def recursion_sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + recursion_sum(nums[1:])
# print(recursion_sum([2,4,5,6,7]))


# 2.) Write a program to calculate the factorial of a number
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)
# print(factorial(10))
