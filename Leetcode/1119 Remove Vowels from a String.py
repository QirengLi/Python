def removeVowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    res = ""
    for char in s:
        if char in vowels:
            continue
        else:
            res += char
    return res

