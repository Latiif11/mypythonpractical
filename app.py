from typing import Any, Union

from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

character_name = "Tom"
character_age = "40"
print("There once was a man named" + character_name + ",")
print("He was " + character_age + " years old."   ",")
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ",")

phrase = "latif Academy"
print(phrase + " is cool")
print(phrase.lower())

### Math
print(4 + 5)
print(10 % 4)
my_num = 5
print(str(my_num) + " Is my fav number")

from math import *

my_num = -5
print(sqrt(36))


def fun(a=12, b=2):
    print(a // 9)
    return (a * b)


fun(a=9, b=2)

print("\n")
import calendar

yy = 2020  # Year
mm = 8  # Month
# To take mont and input from user
# yy = int(input("Enter year:"))
# mm =int(input("Enter a month"))
# Display the calendar
print(calendar.month(yy, mm))
print("\n")

#### Calculater
num1 = input("Enter a number:")
num2 = input("Enter another number:")
result = float(num1) + float(num2)
print(result)
##################
####MADLIBS Game

color = input("Enter a colar:")
plural_noun = input("Enter a Plural Noun:")
Celebrity = input("Enter a Celebrity:")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + Celebrity)
print("\n")
# Lists in python
print("\n")

friends = ["Kevin", "Karen", "Jim"]

print(friends[2])

####List and fucations
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["kevin", "Karen", "Jim", "Oscar", "Tomy"]
friends.pop()
print(friends)

coordinates = (4, 5)
print(coordinates[0])


###Fuction

def sayhi():
    print("Hello User")

sayhi()

#If Statement.

is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a male or tall both")
else:
    print("You are neither male or tall ")

print("\n")
num1 = float(input("Enter fist number:"))
op = input("Enter operator: ")
num2 = float(input("Enter second number"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
     print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid number")
     

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(2, 3))

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7,8,9],
    [0]

]

for row in number_grid:
    for col in row:
     print(row)

def translate(phrase):
    translation = ""
    for letter in phrase:
         if letter in "AEIOasaeiou":
             translation = translation + "g"
         else:
             translation = translation + letter
             return translation

print(translate(input("Etnter a phrase:")))


try:
    number = int(input("Enter a number:"))
    print(number)
except ZeroDivisionError:
    print("Divided by Zero")
except ValueError:
    print("invalid input")



#How to read and a file on python way by non python files

employee_file = open("employee.txt", "r")
for employee in employee_file.readlines():
    print(employee)
print(employee_file.readlines())

employee_file.close()


#Wrote new file and appending

employee_file = open("employee.txt", "w")

print(employee_file.write("\nToby -Human Resources"))

employee_file.close()

#Creating new file

employee_file = open("index.html", "w")

print(employee_file.write("<p>This is page </p>"))

employee_file.close()