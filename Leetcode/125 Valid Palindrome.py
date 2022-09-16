
# Brute force method

def isPalindrome(s):
    newStr = ""
    endIdx = -1

    for i in s:
        if i.isalnum():
            newStr += i.lower()

    for j in range(len(newStr)):
        if newStr[j] != newStr[endIdx]:
            return False
        else:
            endIdx -= 1
    return True

# Optimized method

