def backspaceCompare(s, t):
    stack_s = []
    stack_t = []

    for char in s:
        if char is not "#":
            stack_s.append(char)
        else:
            if not stack_s:
                continue
            stack_s.pop()

    for char in t:
        if char is not "#":
            stack_t.append(char)
        else:
            if not stack_t:
                continue
            stack_t.pop()

    return stack_s == stack_t

# Stack approach - can use a helper function for cleaner code instead of the two for loops
