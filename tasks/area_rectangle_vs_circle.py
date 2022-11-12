# Completed
'''
Circle Vs Rectangle
Circle:
r = 10.6

Rectangle:
a = 1.3
b = ??

Task:
Write program that uses a while loop to find the largest
possible integer b that give a rectangle area smaller than, but as close as possible,
the area of the circle.

Right answer:
b = 271.

Formula:
Area of Rectangle = l x w = a x b
Area of Circle = Phi x r^2 

'''
# Answer
import math
import numpy as np

pi = math.pi
r = 10.6
a = 1.3
area_of_circle = pi*r**2

b = 0
while a*b < area_of_circle:
    b += 1
b -= 1
print('The maximum b is: {b}'.format(b=b))
