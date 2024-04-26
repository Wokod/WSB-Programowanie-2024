#-----------task 1---------------------------------------------------------
def sum_list(items):
    sum = 0
    for x in items:
        sum += x
    return sum
print(sum_list([1,2,3]))

list=[1,2,3]
s = sum(list)
print(s)
#---------------------------------------------------------task 2---------------------------------------------------------
def multiply(list, multiplier):
    for x in range(len(list)):
        list[x] = list[x] * multiplier
    return list
print(multiply([1,2,3], 2))
#---------------------------------------------------------task 3---------------------------------------------------------
def max_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
print(max_in_list([1,5,-3,7]))
#---------------------------------------------------------task 4---------------------------------------------------------
def min_in_list(list):
    min = list[0]
    for a in list:
        if a < min:
            min = a
    return min
print(min_in_list([1,5,-3,7]))
#---------------------------------------------------------task 5---------------------------------------------------------
def check_strings(list):
    x = 0
    for s in list:
        if len(s) > 1 and s[0] == s[-1]:
            x += 1
    return x
print(check_strings(["abc", "abbc", "aa", "12321"]))
#---------------------------------------------------------task 6---------------------------------------------------------
def last(x):
    return x[-1]
def sorted_list(tuples):
    return sorted(tuples, key=last)
print(sorted_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
#---------------------------------------------------------task 7---------------------------------------------------------
list = [1, 2, 2, 3, 5, 0, 0, 5, 9]
duplicate = set()
unique = []
for x in list:
    if x not in duplicate:
        unique.append(x)
        duplicate.add(x)
print(duplicate)
#---------------------------------------------------------task 8---------------------------------------------------------
list = [1]
if not list:
    print("List is empty")
else:
    print("List is not empty")
#---------------------------------------------------------task 9---------------------------------------------------------
list1 = [1, 2, 3]
list2 = list(list1)
print(list1)
print(list2)
#---------------------------------------------------------task 10--------------------------------------------------------
def long(length, str):
    word_len = []
    text = str.split(" ")
    
    for x in text:
        if len(x) > length:
            word_len.append(x)
    return word_len
print(long(3, "test"))
#---------------------------------------------------------task 11--------------------------------------------------------
def similiar(list1, list2):
    x = False
    for y in list1:
        for z in list2:
            if y == z:
                x = True
                return x
print(similiar([1, 2, 3, 4,], [4, 5, 6, 7]))
print(similiar([1,2], [3, 4]))
#---------------------------------------------------------task 12--------------------------------------------------------
items = ['phone', 'car', 'keys', 'wallet', 'laptop', 'motorcycle', 'bike']
items = [x for (i, x) in enumerate(items) if i not in (0, 4, 5)]
print(items)
#---------------------------------------------------------task 13--------------------------------------------------------
array = [[["*" for col in range(6)] for col in range(4)] for row in range(3)]
print(array)
#---------------------------------------------------------task 14--------------------------------------------------------
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = [x for x in list if x % 2 != 0]
print(list)
#---------------------------------------------------------task 15--------------------------------------------------------
from random import shuffle
list = ['car', 'keys', 'bike', 'motorcycle', 'phone', 'wallet']
shuffle(list)
print(list)
#---------------------------------------------------------task 16--------------------------------------------------------
def values():
    list = []
    for i in range(1, 30):
        list.append(i**2)
    print(list[:5])
    print(list[-5:])
values()
#---------------------------------------------------------task 17--------------------------------------------------------
def test(num):
    return all(is_prime(i) for i in num)
def is_prime(y):
    if (y == 1):
        return False
    elif (y==2):
        return True
    else:
        for x in range(2, y):
            if (y % x == 0):
                return False
        return True

print(test([3, 7]))
#---------------------------------------------------------task 18--------------------------------------------------------
import itertools
print(list(itertools.permutations([1, 2, 3])))
#---------------------------------------------------------task 19--------------------------------------------------------
list1 = [1, 2, 3, 4, 5]
list2 = [1, 6, 7, 8, 5]

diff1 = list(set(list1) - set(list2))
diff2 = list(set(list2) - set(list1))

diff3 = diff1 + diff2
print(diff3)
#---------------------------------------------------------task 20--------------------------------------------------------
list = [1, 3, 5, 7, 9]
for num_index, num_val in enumerate(list):
    print(num_index, num_val)