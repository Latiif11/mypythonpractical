# ifex.py
x = 2
# bracketets are not necessary (used for clarity of the code)
if (x%2 == 0): # % sign gives the value of the remainder e.g 5%3 =2
    #if above condition is true, only then following will be exucting
    print('Number is even.')

#This line will execute always as it not inside if
print('Bye Bye')
#ifOnly: uses multiple if to check even and odd number

# 'input' command takes input as string
# int is used for type conversion
x= int(input('Enter the number:\t')) #\t is used for uoput type

# % is used to calculate remainder
if x%2==0:
    print('Number is even ')
else:
       print('Number is odd')

# 'int (input())' command takes input as number
x= int(input('Enter the number: \t'))

# % is used to calculate remainder
if x%2==0: #'check divisibily with 2'
    if x%3==0: # if x%2=0, then check this line
        print("Number is diviible by 2 and 3")
    else:
        print("Numebr is divisible by 3 only")
        print("x%3= ", x%3)
elif x%3==0: #check this if x%2 not zero
    print("Number is diviible by 2 and 3")
else:
    print("Number is not divisible by 2 and 3")
    print("x%2= ", x%2)
    print("x%3=", x%3)
print('Thank you')

#WhileExample1

n=1 #initial value number
print('Numbers upto 5: ')
while n<6:
    print (n, end=""), #end='': to stop row change
    n=n+1
print("\nCode ended at n =  %s" % n)

range(5)
[0, 1, 3, 4]

range(1,4)
[1, 2, 3]

range(11, 19, 2)
[11, 13, 15, 17]

range(15, 7, -2)
[15, 13, 11, 9]

#forexample1.py print number 1-5

print("print in forward order")
for i in range(5):
    print(i+1, end= " ")
print('\nfinal value of i is ', i)

print('\nNumber in reverse order')
for j in range(5, 0, -1):
    print(j, end=" "),
print("\nfina value of i is: ", j)


fruits=["Apple", "Banana", "Orange"]
print("List of fruits are shown below:")
for i in fruits:
    print(i)



