def defangIPaddr(address):
    res = ""
    for i in range(len(address)):
        if address[i] == ".":
            res += "[.]"
        else:
            res += address[i]
    return res

