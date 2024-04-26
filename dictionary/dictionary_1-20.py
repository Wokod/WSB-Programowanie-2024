#---------------------------------------------------------task 1---------------------------------------------------------
new_dict = { 1 : 10, 2 : 13, 3 : 7, 4 : 12}
print(new_dict)
sorted1 = dict(sorted(new_dict.items(), key=lambda item:item[1]))
print(sorted1)
sorted2 = dict(sorted(new_dict.items(), key=lambda item:item[1], reverse=True))
print(sorted2)
#---------------------------------------------------------task 2---------------------------------------------------------
new_dict = { 1 : 10, 2 : 13, 3 : 7, 4 : 12}
new_dict.update({5: 17})
print(new_dict)
#---------------------------------------------------------task 3---------------------------------------------------------
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}

for d in (dic1, dic2, dic3): 
    dic4.update(d)
print(dic4)
#---------------------------------------------------------task 4---------------------------------------------------------
dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
 
def check(x):
    if x in dic:
        print("Yes")
    else:
        print("No")
check(7)
#---------------------------------------------------------task 5---------------------------------------------------------
dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for key, value in dic.items():
    print(key, "->", value)
#---------------------------------------------------------task 6---------------------------------------------------------
x = int(input("Give a number: "))
d = dict()

for y in range(1, x + 1):
    d[y] = y * y
print(d)
#---------------------------------------------------------task 7---------------------------------------------------------
d = dict()

for x in range(1, 16):
    d[x] = x * x
print(d)
#---------------------------------------------------------task 8---------------------------------------------------------
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = dic1.copy()
dic3.update(dic2)
print(dic3)
#---------------------------------------------------------task 9---------------------------------------------------------
dic = {1: 10, 2: 20, 3: 30, 4:40}

for key, value in dic.items():
    print(key, "value is:", dic[key])
#---------------------------------------------------------task 10--------------------------------------------------------
dic = {1: 10, 2: 20, 3: 30, 4:40}
x = sum(dic.values())
print(x)
#---------------------------------------------------------task 11--------------------------------------------------------
dic = {1: 10, 2: 20, 3: 30, 4:40}
x = 1
for key in dic:
    x = x * dic[key]
print(x)
#---------------------------------------------------------task 12--------------------------------------------------------
dic = {"a": 10, "b": 20, "c": 30, "d":40}
if 'a' in dic:
   del dic["a"]
print(dic)
#---------------------------------------------------------task 13--------------------------------------------------------
keys = ["1", "2", "3", "4"]
values = ["car", "wallet", "phone", "computer"]

items = dict(zip(keys, values))

print(items)
#---------------------------------------------------------task 14--------------------------------------------------------
colors = {'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': '#FFFFFF'}
for key in sorted(colors):
    print(key, colors[key])
#---------------------------------------------------------task 15--------------------------------------------------------
dic = {"a": 100, "b": 20, "c": 30, "d":-40}
key_max = max(dic.keys(), key=(lambda k: dic[k]))
key_min = min(dic.keys(), key=(lambda k: dic[k]))

print("Max value: ", dic[key_max])
print("Min value: ", dic[key_min])
#---------------------------------------------------------task 16--------------------------------------------------------
dic = {"a": 10, "b": 20, "c": 30, "d":40, "e": 1, "f": 20, "g": 3, "h":40}
unique = {}
for key, value in dic.items():
    if value not in unique.values():
        unique[key] = value
print(unique)
#---------------------------------------------------------task 17--------------------------------------------------------
dic = {}
if not dic:
    print("Empty")
else:
    print("Not empty")
#---------------------------------------------------------task 18--------------------------------------------------------
dic1 = {"a": 10, "b": 20, "c": 30, "d": 40}
dic2 = {"a": 5, "b": 10, "c": 15, "d": 20, "e": 25}

dic3 = {}

for key, value in dic1.items():
    dic3[key] = value

for key,value in dic2.items():
    if key not in dic3:
        dic3[key] = value
    else:
        dic3[key] += value

print(dic3)
#---------------------------------------------------------task 19--------------------------------------------------------
dic = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
unique = set()
for key in dic:
    for value in key.values():
        unique.add(value)
print(unique)
#---------------------------------------------------------task 20--------------------------------------------------------
from heapq import nlargest

dic = {'a': 5, 'b': 50, 'c': 15, 'd': 25, 'e': -10, 'f': 35}

top_three = nlargest(3, dic, key=dic.get)

print(top_three)