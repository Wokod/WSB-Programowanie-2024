#---------------------------------------------------------task 1=--------------------------------------------------------
list1 = []
for x in range (1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        list1.append(str(x))
print(".".join(list1))
#---------------------------------------------------------task 2=--------------------------------------------------------
T = input("What is the temperature? (e.g., 24C, 80F etc.)")

D = int(T[:-1])

Convert = T[-1]

if Convert.upper() == "C":
    result = int(round((9*D) / 5 + 32))
    Converted = "Fahrenheit"
elif Convert.upper() == "F":
    result = int(round((D - 32) * 5 /9))
    Converted = "Celsius"
else:
    print("Provide proper data")
    quit()
print("Temperature in ", Converted, "is ", result, "degrees")
#---------------------------------------------------------task 3=--------------------------------------------------------
import random

x, y = random.randint(1,10),0

while x != y:
    y = int(input("Guesss number: "))
print("You are right!")
#---------------------------------------------------------task 4=--------------------------------------------------------
for x in range (5):
    for y in range(x):
        print("* ", end="")
    print("")
for x in range(5, 0, -1):
    for y in range(x):
        print("* ", end="")
    print("")
#---------------------------------------------------------task 5=--------------------------------------------------------
x = 3
for y in range (x):
    for z in range(y):
        print("* ", end="")
    print("")
for y in range(x, 0, -1):
    for z in range(y):
        print("* ", end="")
    print("")
#---------------------------------------------------------task 6=--------------------------------------------------------
word = input("Give a word: ")
for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")
print("\n)")
#---------------------------------------------------------task 7=--------------------------------------------------------
list = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd = 0
even = 0

for x in list:
    if not x % 2:
        odd +=1
    else:
        even +=1
print("Odds: ", odd)
print("Even: ", even)
#---------------------------------------------------------task 8=--------------------------------------------------------
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for x in datalist:
    print("Type", x, type(x))
#---------------------------------------------------------task 9=--------------------------------------------------------
for x in range(1, 7):
    if x != 3 and x != 6:
        print(x)
#---------------------------------------------------------task 10--------------------------------------------------------
x = 0
y = 1

while y < 50:
    print(y)
    x, y = y, x + y
#---------------------------------------------------------task 11--------------------------------------------------------
for x in range(1, 51):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
        continue
    elif x % 3 == 0:
        print("Fizz")
        continue
    elif x % 5 == 0:
        print("Buzz")
        continue
    print(x)
#---------------------------------------------------------task 12--------------------------------------------------------
rows = int(input("Number of rows: "))
columns = int(input("Number of columns: "))

a = [[0 for _ in range(columns)] for _ in range(rows)]
for row in range(rows):
    for col in range(columns):
        a[row][col] = (row + 1) * (col + 1)
print(a)
#---------------------------------------------------------task 13--------------------------------------------------------
binary_numbers = input("Enter a sequence of binary numbers separated by commas: ")

numbers = binary_numbers.split(',')
divisible_by_5 = []
for number in numbers:
    decimal_number = int(number, 2)
    if decimal_number % 5 == 0:
        divisible_by_5.append(number)

print("Numbers divisible by 5  5: ", ','.join(divisible_by_5))
#---------------------------------------------------------task 14--------------------------------------------------------
str = input("Give a string: ")
d = 0
l = 0

for x in str:
    if x.isdigit():
        d += 1
    elif x.isalpha():
        l += 1
    else:
        pass
print("Letters:", l)
print("Digits:", d)
#---------------------------------------------------------task 15--------------------------------------------------------
import re
p = input("Input your password: ")
x = True
while x:  
    if (len(p) < 6 or len(p) > 12):
        break

    elif not re.search("[a-z]", p):
        break
    elif not re.search("[0-9]", p):
        break
    elif not re.search("[A-Z]", p):
        break
    elif not re.search("[$#@]", p):
        break
    elif re.search("\s", p):
        break
    else:
        print("Good Password")
        x = False
        break
if x:
    print("Badd Password")
#---------------------------------------------------------task 16--------------------------------------------------------
list = []
for i in range(100, 401):
    s = str(i)
    
    if (int(s[0]) % 2 == 0) and (int(s[1]) %2 == 0) and (int(s[2]) % 2 == 0):
        list.append(s)
print(",".join(list))
#---------------------------------------------------------task 17--------------------------------------------------------
result_str = ""
for row in range(7):
    for column in range(7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (1 < column < 5))):
            result_str += "*"
        else:
            result_str += " "
    result_str += "\n"

print(result_str)
#---------------------------------------------------------task 18--------------------------------------------------------
result_str = ""
for row in range(7):
    for column in range(7):
        if (column == 1 or ((row == 0 or row == 6) and (1 < column < 5)) or (column == 5 and (0 < row < 6))):
            result_str += "*"
        else:
            result_str += " "
    result_str += "\n"

print(result_str)
#---------------------------------------------------------task 19--------------------------------------------------------
result_str = ""
for row in range(7):
    for column in range(7):
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):
            result_str += "*"
        else:
            result_str += " "
    result_str += "\n"

print(result_str)
#---------------------------------------------------------task 20--------------------------------------------------------
result_str = ""
for row in range(7):
    for column in range(7):
        if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):
            result_str = result_str + "*"
        else:
            result_str += " "
    result_str += "\n"

print(result_str)
