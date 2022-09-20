def isPowerOfTwo(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n /= 2
    return n == 1

# Iteritive approach
# Will continue to divide the number by 2 until there is a remainder
# then it will return true or false whether that number is equal to 1