def isAnagram(s, t):
    str_dict = {}

    for i in s:
        if i in str_dict:
            str_dict[i] += 1
        else:
            str_dict[i] = 1

    for j in t:
        if j in str_dict:
            if str_dict.get(j) == 1:
                str_dict.pop(j)
            else:
                str_dict[j] -= 1
        else:
            return False

    if len(str_dict) != 0:
        return False

    return True

# Above is a slightly more optimized solution
# main difference lies in the 2nd for loop where if the value/count of the character is at 1
# it will remove it from the dictionary. Then we can check the length of the dictionary to see if
# it's empty.

# Below function doesn't remove anything from the dictionary but instead, subtracts the count
# of the chars and then checks all the values to see if it equals 0

# both solutions are space and time complexity of O(n)

def isAnagram(s, t):
    str_dict = {}

    for i in s:
        if i in str_dict:
            str_dict[i] += 1
        else:
            str_dict[i] = 1

    for j in t:
        if j in str_dict:
            str_dict[j] -= 1
        else:
            return False

    for vals in str_dict.values():
        if vals != 0:
            return False

    return True