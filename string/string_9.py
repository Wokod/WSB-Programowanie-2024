def remove(str, x):
    first = str[:x]
    last = str[x+1:]
    return first + last
print(remove("Dominik", 3))