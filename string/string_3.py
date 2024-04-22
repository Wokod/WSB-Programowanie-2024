
def string_both_ends(str):
    if len(str) >= 2:
        return str[0:2] + str[-2:]
    else:
        return ''
print(string_both_ends('test'))
print(string_both_ends('tes'))
print(string_both_ends('te'))
print(string_both_ends('t'))