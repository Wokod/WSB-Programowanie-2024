def change(str):
    char = str[0]
    str = str.replace(char, '$')
    str = char + str[1:]
    return str
print(change('dodolod'))