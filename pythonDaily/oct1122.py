import numpy as np
# BOOK: Linge, Svein; Hans Petter Langtangen. Programming for Computations - Python: 15 (Texts in Computational Science and Engineering) (p. 65). Springer International Publishing. Kindle Edition.

# Loop and Branching
""" Notes:

for loop_variable in some_numbers:
     <code line 1>
     <code line 2>
     
for loop_variable in range(start, stop, step):

"""

# 3.1 The for loop
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print ('{:d}+5 = {:d}'.format(i,i+5))
    
    
for i in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:
    print ('{:d}+5 = {:d}'.format(i,i+5))
    
    
for i in [1, 2, 3]:
    print('i = {:d}'.format(i))
    for j in [4.0, 5.0, 6.0]:
        print('     j={:1f}'.format(j))
        

for i, j, k in (1, 2, 3), (4, 5, 6), (6, 7, 8):
    print(i, j, k)
    

N = 5
h = np.zeros(N)
h[0] = 1.60
h[1] = 1.85
h[2] = 1.75
h[3] = 1.80
h[4] = 0.50
sum = 0
for i in [0, 1, 2, 3, 4]:
    sum = sum + h[i]
average = sum/N
print('Average height: {:g}'.format(average))


x = range(0, 5, 1)
print(type(x))


for i in range(0, 5, 1):
    print(i)
    

listA = list(range(1, 11, 1))
listB = list(range(1, 11))
listC = list(range(11))
listD = list(range(1, -11, -1))
print('{listA}, \n{listB}, \n{listC}, \n{listD}'.format(listA=listA, listB=listB, listC=listC, listD=listD))