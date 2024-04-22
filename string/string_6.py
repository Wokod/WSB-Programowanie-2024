def ending(str1):
    if len(str1) < 3:
        return str1
    elif str1[-3:] == "ing":
         str1 = str1 + "ly"
    else:
         str1 = str1 + "ing"
    return str1
print(ending("abcd"))