#FunEx.py
def addTwoNum(a,b):
    sum = a+b
    return (sum)

result = addTwoNum(3,4)
print("sum of numbers is %s" % result)

#FuncExr2.py: default argument can be defined only after non-default argument
# e.g addTwoNum(num1=2 num2): is wrong be must have sime defined value

def addTwoNum(num1, num2=2):
    return (num1+num2)

result1 = addTwoNum(3)
print('result1=%s' % result1)

result2 = addTwoNum(3,4)
print("result2=%s" % result2)
