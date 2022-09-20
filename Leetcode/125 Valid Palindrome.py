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

def isPalindrome(s):

    l = 0
    r = len(s) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
    return True
