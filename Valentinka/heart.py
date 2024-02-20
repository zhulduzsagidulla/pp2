import math 
from turtle import *
speed(10**100)
bgcolor("black")
def heart1(a):
 return 12*math.sin(a)**3
def heart2(b):
    return 10*math.cos(b)-5*\
    math.cos(2*b)-2*\
    math.cos(3*b)-\
    math.cos(4*b)
for i in range (6000):
    goto(heart1(i)*20,heart2(i)*20)
    for i in range (5):
        color("#f73480")
    goto (0,0)
done()