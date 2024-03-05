#1
import math

from math import pi
degree = int(input())
radian = degree * pi/180
print(radian)

#2
h = int(input())
a = int(input())
b = int(input())
s = (a+b)/2*h
print(s)


#3
from math import pi, tan
n = int(input())
side = int(input())
area = n * (side ** 2) / (4 * tan(pi / n))
print(area)

#4
base = 5
height = 6
print(base * height)