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