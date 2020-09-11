xString = input("Enter a number:")
x = int(xString)
yString =input("Enter a Second numbe:")
y = - int(yString)
print('The sum of ', x, 'and ', y, 'is', x+y, '.', sep='')

'''Compare print with concatenation and with format string'''
applicant = input("Enter the applicant's name:")
interviewer = input("Enter the interviewer's name: ")
time = input("Enter the appointment time:")
print(interviewer + ' will interview ' + applicant + 'at' + time +'.')
print(interviewer + ' will interview ' , applicant , 'at' , time, '.', sep='')
print('{} will interview {} at {}.' .format(interviewer, applicant, time) )


'''Illustrate a global constant being used inside functions.'''
PI = 3.14159265358979 # global constant -- only place the value of PI is set
def circleArea(radius):
    return PI*radius*radius # use value of global constant PI
def circleCircumference(radius):
    return 2*PI*radius # use value of global constant PI
def main():
 print('circle area with radius 5:', circleArea(5))
 print('circumference with radius 5:', circleCircumference(5))

main()