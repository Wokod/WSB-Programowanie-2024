def odd(str):
    result = ""
    x = 0
    while x < len(str):
        if x % 2 == 0:
            result = result +str[x]
        x += 1
    return result
print(odd("abcdefghijk"))