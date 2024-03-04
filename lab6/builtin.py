#1

def mylist(my):

    result = 1
    for x in my:
        result=result*x
    return result 
list1= [1,2,3,4,5]

print(mylist(list1))

from functools import reduce
list = [1,2,3,4]
result = reduce(lambda x,y: x*y , list)
print(result)

#2

def strn(s):
    upper=0
    lower=0
    for i in s:
        if(i.isupper()):
            upper+=1
        if(i.islower()):
            lower+=1
    return upper,lower
s=input()
print(strn(s))

#3
def strn(s):
    if(s==s[::-1]):
        return "yes"
    else:
        return "no"
s=input()
print(strn(s))

#4
import math
import time 
def root(number, ms):

    result = math.sqrt(number)
    return result

number =int(input())
ms = int(input())

time.sleep(ms/1000)
result = root(number, ms)


print(f"Square root of {number} after {ms} milliseconds is {result}")

#5
list = [1,2,3,0]
print(all(list))