def remove(str):
    first = str[:1]
    last = str[-1:]
    return last + str[1:-1] + first
print(remove("1234"))