def isValid(s):

    stack = []
    para_dict = {")": "(", "}": "{", "]": "["}

    for elem in s:
        if elem in para_dict:
            if stack and stack[-1] == para_dict[elem]:
                stack.pop()
            else:
                return False
        else:
            stack.append(elem)

    return not stack
