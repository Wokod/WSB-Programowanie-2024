def change(str1, str2):
    chars1 = str1[:2]
    chars2 = str2[:2]
    str1 = chars2 + str1[2:]
    str2 = chars1 + str2[2:]
    return str1 + " " + str2
print(change("abcd", "fghi"))