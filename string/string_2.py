#Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
def frequency(str):
    dict = {}
    for x in str:
        keys = dict.keys()
        if x in keys:
            dict[x] += 1
        else:
            dict[x] = 1
    return dict
print(frequency('Dominik Kowalski'))