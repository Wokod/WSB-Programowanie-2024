#---------------------------------------------------------task 1=--------------------------------------------------------
def string_length(str):
    return len(str)
print(string_length('test')) 
#---------------------------------------------------------task 2=--------------------------------------------------------
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
#---------------------------------------------------------task 3=--------------------------------------------------------
def string_both_ends(str):
    if len(str) >= 2:
        return str[0:2] + str[-2:]
    else:
        return ''
print(string_both_ends('test'))
print(string_both_ends('tes'))
print(string_both_ends('te'))
print(string_both_ends('t'))
#---------------------------------------------------------task 4=--------------------------------------------------------
def change(str):
    char = str[0]
    str = str.replace(char, '$')
    str = char + str[1:]
    return str
print(change('dodolod'))
#---------------------------------------------------------task 5=--------------------------------------------------------
def change(str1, str2):
    chars1 = str1[:2]
    chars2 = str2[:2]
    str1 = chars2 + str1[2:]
    str2 = chars1 + str2[2:]
    return str1 + " " + str2
print(change("abcd", "fghi"))
#---------------------------------------------------------task 6=--------------------------------------------------------
def ending(str1):
    if len(str1) < 3:
        return str1
    elif str1[-3:] == "ing":
         str1 = str1 + "ly"
    else:
         str1 = str1 + "ing"
    return str1
print(ending("abcd"))
#---------------------------------------------------------task 7=--------------------------------------------------------
def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')
    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor+len('poor'))], 'good')
        return str1
    else:
        return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor !'))
#---------------------------------------------------------task 8=--------------------------------------------------------
def longest(words):
    word_len=[]
    for x in words:
        word_len.append((len(x), x))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
longest_length, longest_word = longest(["abc", "defg", "hi"])
print("Longest word: ", longest_word)
print("Length of the longest word: ", longest_length)
#---------------------------------------------------------task 9=--------------------------------------------------------
def remove(str, x):
    first = str[:x]
    last = str[x+1:]
    return first + last
print(remove("Dominik", 3))
#---------------------------------------------------------task 10=-------------------------------------------------------
def remove(str):
    first = str[:1]
    last = str[-1:]
    return last + str[1:-1] + first
print(remove("1234"))
#---------------------------------------------------------task 11=-------------------------------------------------------
def odd(str):
    result = ""
    x = 0
    while x < len(str):
        if x % 2 == 0:
            result = result +str[x]
        x += 1
    return result
print(odd("abcdefghijk"))
#---------------------------------------------------------task 12=-------------------------------------------------------
def word_counter(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(word_counter("dzien pierwszy dzien drugi dzien trzeci czwarty weekend weekend weekend"))
#---------------------------------------------------------task 13=-------------------------------------------------------
word = input("Provide data: ")
print("Upper data: ", word.upper())
print("Lower data: ", word.lower())
#---------------------------------------------------------task 14=-------------------------------------------------------
data = input("Provide comma-separated words: ")
animals = [name.strip() for name in data.split('.')]
print(" ".join(sorted(list(set(animals)))))
#---------------------------------------------------------task 15=-------------------------------------------------------
word = input("Give your word: ")
def multiply(word):
    sub_str = word[-2:]
    return sub_str * 4
print(multiply(word))
#---------------------------------------------------------task 16=-------------------------------------------------------
def first(str):
    if len(str) <= 3:
        return str
    else :
        return str[:3]
print(first("testtest"))
#---------------------------------------------------------task 17=-------------------------------------------------------
def reverse(s):
    if len(s) % 4 == 0:
        return " ".join(reversed(s))
    return s
print(reverse("abcdefgh"))
print(reverse("abdef"))
#---------------------------------------------------------task 18=-------------------------------------------------------
import textwrap
data = "test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test "
print()
print(textwrap.fill(data, width=50))
print()
#---------------------------------------------------------task 19=-------------------------------------------------------
area = 1256.66
volume = 1254.725
decimals = 2
print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))
decimals = 3
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))
#---------------------------------------------------------task 20=-------------------------------------------------------
data = '''
    test test test
test test test
        test test test
test test test
                test test test
test test test
'''
prefix = ">"
text_with_prefix = '\n'.join(prefix + " " + line.lstrip() for line in data.split('\n'))

print()
print(text_with_prefix)
print()