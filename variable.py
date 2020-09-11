####vari,e 3 with 6ableer.py a nad b are variables
#which store 3  and 5 respectively
a=3
b=6
### fallowint line will be add value of a i
print(a+6) #9
print((a+b)/2)
print(int(a+b)/2)

#Numberformating
a = 11 #integer
print(hex(a))

b= 3.2 #floating
print(oct(int(b)))

d = 0X1A
print(d)

##add hex and float
print(b+d)

c = 0o17
print(c)
#T see octal form use 'oct'
print(oct(c))

e = 3+2j #imagenary
print(abs(e))
print(abs(e),2)
r = round(abs(e),2)

#1.3.6 String
#StrnEr
fistname = 'hand'
print(fistname)
fullname = 'hanad abdi'
print(fullname)
#input is used to take input from user
score1 = input('Enter the score 1: ')
score2 = input('Enter the score 2 :')
totalString = score1 + score2
messageString = 'Total score is %s'
#in below print, totallstring will be assing to  %s
print(messageString % totalString)

#score1 and score2 are saved as string above
totalInt = int(score1) + int(score2)
messageString = 'Total score is %s'
print(messageString % totalInt)

#Chanage the input as interger immedaitely
score1 = int(input("Enter the score 1: "))
score2 = int(input("Enter the score 2: "))
total = score1 + score2
messageString = "score1 (%s) + score2[%s] =   %s"
print(messageString % (score1, score1, total))

#List

a = [24, 'as it is', 'abc', 2+2j]
# inder start with 0
# i,e. location of number 24 us 0' in the list
print(a[0]) #24
print(a[2]) #abc

#replace 'abc' with 'xyz'
a[2] ='xyz'
print(a[2])

#Add 20 at the end of lis
a.append(20)
print(a)


####Tuple
a = 24, 'as it is ', 'abc', 2+2j
##Some times () bracjets are used to define tuples
#a = (24, ''as it is), 'abc', 2+2j)
#inder start with 0
#i.e. Location of number 24 is '0' in the list
print(a[0]) # 24
print(a[2]) # abc

### following lines will give error,

##as value can be chanaged in tuple


